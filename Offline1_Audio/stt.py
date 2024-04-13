import json
from vosk import Model, KaldiRecognizer
import wave
import sys
sys.path.append('..')
from tools.mic import record_audio

def stt(filename="output.wav", duration=3, model_path="/home/pi/RobotV2/Offline1_Audio/vosk-model-small-cn-0.22"):
    # 输入模型路径
    model = Model(model_path)
    
    # 准备录音
    record_audio(filename, duration)  
    wf = wave.open(filename, 'rb')
    
    # 初始化识别器
    rec = KaldiRecognizer(model, wf.getframerate())
    
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)
    
    text = json.loads(rec.FinalResult())
    
    result = text.get('text', '').replace(' ', '')
    
    return result

if __name__ == "__main__":
    """
        - model_path 模型所在的文件夹路径
        - duration 录制持续时间（秒）
    """
    result = ""  # 初始化result变量
    while result != "结束表演":
        result = stt()
        print(result)
