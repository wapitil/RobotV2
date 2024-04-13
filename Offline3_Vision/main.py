import os 
from process import predict
import time
from collections import Counter
import cv2
from process import capture_image

if __name__=="__main__":
    class_names = ["站立", "大字站", "弓箭步", "举双手", "蹲马步", "叉腰", "挥手"]
    # 要检测的文件夹
    images_in_folder = "my_data"
    # 处理后的文件夹和csv文件的输出路径
    images_out_folder = "processed_images"
    csv_out_path = "processed_data.csv"
    # 创建输出目录（如果不存在）
    os.makedirs(images_out_folder, exist_ok=True)

    cap = cv2.VideoCapture(0)
    try:
        for i in range(6):
            capture_image(cap,i)
            time.sleep(0.5)
        result=predict(class_names,images_in_folder, images_out_folder, csv_out_path)
        # 统计预测结果
        result_counts = Counter(result)
        most_common_result, count = result_counts.most_common(1)[0]
        if count > 3:
            print(f"主要预测结果：{most_common_result}")
    finally:
      cap.release()
