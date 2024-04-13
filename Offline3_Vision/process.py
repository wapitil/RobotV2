import csv
import cv2
import numpy as np
import pandas as pd
import os
import tqdm
from matplotlib import pyplot as plt
import tflite_runtime.interpreter as tflite
import utils
from ml import Movenet
# Load MoveNet Lightning model
movenet = Movenet('movenet_lightning')

def detect(input_tensor, inference_count=3):
  """Runs detection on an input image.

  Args:
    input_tensor: 这是一个表示输入图像的 TensorFlow 张量，其维度为 [height, width, 3]，
    数据类型为 tf.float32。
    inference_count: 此参数指定模型应在相同输入图像上运行多少次，以提高检测准确性。
    默认值设置为 3。

  Returns:
    返回 MoveNet.SinglePose 模型检测到的 "Person" 实体
  """
  # 函数从输入张量中提取了高度、宽度和通道信息。
  image_height, image_width, channel = input_tensor.shape

  # 首次使用整个输入图像进行姿势检测[2]
  movenet.detect(input_tensor, reset_crop_region=True)

  # 在每次迭代中，使用 reset_crop_region=False 调用 detect 方法
  # 表明使用上一次检测中识别的感兴趣区域来裁剪图像，以提高准确性。
  for _ in range(inference_count - 1):
    person = movenet.detect(input_tensor,
                            reset_crop_region=False)

  return person

def draw(
        image, person, crop_region=None, close_figure=True,
        keep_input_size=False):
  """Draws the keypoint predictions on image.

  Args:
    image: 一个形状为 [height, width, channel] 的 NumPy 数组.
    person: 从 MoveNet.SinglePose 模型返回的一个人物实体，包含姿势关键点的预测结果.
    crop_region: 一个可选参数，指定感兴趣区域（ROI）.
    close_figure: 一个布尔值，指示在函数返回后是否关闭 plt 图.
    keep_input_size: 一个布尔值，指示是否保持输入图像的大小.

  Returns:
    函数返回包含关键点预测的图像数组 with shape [out_height, out_width, channel] 
  """
  # Draw the detection result on top of the image.
  image_np = utils.visualize(image, [person])

  # 创建图像和轴对象：
  height, width, channel = image.shape
  aspect_ratio = float(width) / height
  fig, ax = plt.subplots(figsize=(12 * aspect_ratio, 12))
  im = ax.imshow(image_np)

  if close_figure:
    plt.close(fig)

 # 　如果 keep_input_size 参数为 False，则调整图像大小，使其保持纵横比并适应指定的大小。
 # not 表示布尔值取反
  if not keep_input_size:
    image_np = utils.keep_aspect_ratio_resizer(image_np, (512, 512))

  return image_np

class MoveNetPreprocessor(object):
    """Helper class to preprocess pose sample images for classification."""

    def __init__(self, images_in_folder, images_out_folder, csvs_out_path):
        """Creates a preprocessor to detection pose from images and save as CSV."""
        self._images_in_folder = images_in_folder
        self._images_out_folder = images_out_folder
        self._csvs_out_path = csvs_out_path
        self._messages = []

        if not os.path.exists(self._images_out_folder):
            os.makedirs(self._images_out_folder)  # 如果输出文件夹不存在，则创建

    def process(self, detection_threshold=0.1):
        """Preprocesses images in the given folder."""
        image_names = sorted([n for n in os.listdir(self._images_in_folder) if not n.startswith('.')])

        # 打开CSV文件用于写入
        with open(self._csvs_out_path, 'w') as csv_out_file:
            csv_out_writer = csv.writer(csv_out_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            for image_name in tqdm.tqdm(image_names):
                image_path = os.path.join(self._images_in_folder, image_name)
                # 尝试读取和处理图像
                try:
                  # 使用OpenCV读取图像
                  image = cv2.imread(image_path)
                  if image is None:
                      raise ValueError("Image not found")
                  # 将BGR图像转换为RGB
                  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                  # 获取图像尺寸
                  image_height, image_width, channel = image.shape
                except Exception as e:
                    self._messages.append(f'Skipped {image_path}. Reason: {str(e)}')
                    continue
                person = detect(image)  # 调用检测函数
                if person is None:  # 检测失败
                    self._messages.append(f"Skipped {image_path}. No pose was confidently detected.")
                    continue

                output_overlay = draw(image.astype(np.uint8), person, close_figure=True, keep_input_size=True)
                output_frame = cv2.cvtColor(output_overlay, cv2.COLOR_RGB2BGR)
                cv2.imwrite(os.path.join(self._images_out_folder, image_name), output_frame)

                pose_landmarks = np.array([[keypoint.coordinate.x, keypoint.coordinate.y, keypoint.score]
                                            for keypoint in person.keypoints], dtype=np.float32)
                coordinates = pose_landmarks.flatten().astype(str).tolist()
                csv_out_writer.writerow([image_name] + coordinates)

        # 打印在图像预处理期间收集的错误消息
        print('\n'.join(self._messages))

def load_csv(csv_path):
    # 加载 CSV 文件：
    dataframe = pd.read_csv(csv_path,header=None)
    # print("Loaded dataframe shape:", dataframe.shape)  # 打印加载后的DataFrame形状
    # CSV 文件的前51列是关键点数据
    X = dataframe.iloc[:, 1:52].astype('float32')  # 跳过第一列（文件名），直接加载关键点数据

    return X, dataframe

def predict(class_names,images_in_folder, images_out_folder, csv_out_path):
  predictions = []
  # 创建并配置预处理器
  preprocessor = MoveNetPreprocessor(images_in_folder, images_out_folder, csv_out_path)

  # 处理目录中的所有图像
  preprocessor.process()
  X_test, _= load_csv(csv_out_path)
  # print(X_test.shape)
  X_test_np = X_test.to_numpy()

  # 加载TFLite模型并分配张量（tensor）
  interpreter = tflite.Interpreter(model_path="my_model.tflite")# 树莓派使用轻量化
  interpreter.allocate_tensors()

  # 获取输入和输出张量的详细信息
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()


  for i, test_sample in enumerate(X_test_np):
      # 确保输入数据的形状匹配模型的输入期望
      test_sample = np.expand_dims(test_sample, axis=0).astype(input_details[0]['dtype'])
      
      # 设置输入张量
      interpreter.set_tensor(input_details[0]['index'], test_sample)
      
      # 调用模型
      interpreter.invoke()
      
      # 获取预测结果
      output_data = interpreter.get_tensor(output_details[0]['index'])
      # print(output_data)
      
      # 获取概率最高的类别索引
      predicted_class_index = np.argmax(output_data)
      
      # 将类别索引转换为类别名称，假设class_names已经定义
      predicted_class_name = class_names[predicted_class_index]
      
      print(f"Sample {i}: Predicted class is '{predicted_class_name}'")
      predictions.append(predicted_class_name)

  return predictions

def capture_image(cap,index):
    """捕获单张图像并保存"""
    ret, frame = cap.read()
    if ret:
        img_path = f'my_data/captured_frame_{index}.jpg'
        cv2.imwrite(img_path, frame)
        return img_path
    return None

