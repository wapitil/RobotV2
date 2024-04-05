import librosa
import soundfile as sf
import numpy as np
import math
import os

def split_audio(file_path, output_dir, segment_length=8, prefix=""):
    """
    将音频文件切割成指定长度的片段并保存到指定目录。
    
    参数:
    - file_path: 音频文件的路径。
    - output_dir: 切割后的片段保存的目录。
    - segment_length: 每个片段的长度，单位为秒。
    - prefix: 每个输出文件名的前缀。
    """
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 加载音频文件
    y, sr = librosa.load(file_path, sr=None)
    
    # 计算每个片段包含的样本数
    samples_per_segment = segment_length * sr
    
    # 计算总共可以切割出多少个完整的片段
    total_segments = int(math.floor(len(y) / samples_per_segment))
    
    # 获取原始文件的基本名称，用于生成输出文件名
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    
    # 逐个片段进行处理
    for segment in range(total_segments):
        start_sample = segment * samples_per_segment
        end_sample = start_sample + samples_per_segment
        
        # 切割音频片段
        segment_samples = y[start_sample:end_sample]
        
        # 保存切割后的片段
        output_filename = os.path.join(output_dir, f"{prefix}{base_filename}_{segment}.wav")
        sf.write(output_filename, segment_samples, sr)
        print(f"Saved: {output_filename}")

def process_directory(input_dir, output_dir, segment_length=8):
    """
    遍历指定目录，切割所有音频文件并保存到输出目录。
    
    参数:
    - input_dir: 输入目录，包含要切割的音频文件。
    - output_dir: 输出目录，用于保存切割后的片段。
    - segment_length: 每个片段的长度，单位为秒。
    """
    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # 检查文件是否为wav格式
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                # 使用文件的基本名称作为前缀
                prefix = "0_"  # 所有片段的文件名将以此前缀开始
                split_audio(file_path, output_dir, segment_length, prefix)

# 示例使用
if __name__ == "__main__":
    input_dir = r"D:\Robot2Pi\Offline2_Music\noise"  # 替换为包含音频文件的目录路径
    output_dir = r"D:\Robot2Pi\Offline2_Music\Music_wav"  # 替换为保存切割后文件的目录路径
    process_directory(input_dir, output_dir)
