import tflite_runtime.interpreter as tflite
import numpy as np
from process import extract_features
import sys
sys.path.append('..')
from tools.mic import record_audio

import warnings
warnings.filterwarnings("ignore")

# TensorFlow Lite模型加载函数
def load_model_tflite(model_path):
    # 加载TFLite模型并分配张量（tensor）
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

# 预测函数，适配TFLite模型
def predict_tflite(file_path, interpreter, sample_rate=48000):
    # 提取特征
    mfccs_processed = extract_features(file_path, sample_rate)
    mfccs_processed = np.expand_dims(mfccs_processed, axis=0).astype(np.float32)

    # 获取输入和输出张量
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    # 使用数据点调用模型
    interpreter.set_tensor(input_details[0]['index'], mfccs_processed)
    interpreter.invoke()
    
    # 获取预测结果
    predictions = interpreter.get_tensor(output_details[0]['index'])
    
    predicted_index = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions, axis=1)[0]
    
    predicted_label = label_to_song[predicted_index]
    return predicted_label, confidence

label_to_song = {
    0: "其他",
    1: "Satisfied",
    2: "Warriors",
    3: "You Didn’t Know",
    4: "Believer",
    5: "Can I Kiss You",
    6: "You",
}

# 使用示例
if __name__ == "__main__":
    # 加载TFLite模型
    interpreter = load_model_tflite("audio_model.tflite")
    
    # 假定已经有录音的.wav文件
    filename = "output.wav"
    record_audio(filename, duration=8)
    predicted_label, confidence = predict_tflite(filename, interpreter)
    print(f"Predicted label: {predicted_label}, Confidence: {confidence}")
