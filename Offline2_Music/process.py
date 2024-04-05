import librosa

import numpy as np
def extract_features(file_path, sample_rate=16000):
    # 加载音频文件，`sr`参数确定了目标采样率
    y, sr = librosa.load(file_path, sr=sample_rate)
    # 接下来，进行MFCC提取特征
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T,axis=0)
    return mfccs_processed