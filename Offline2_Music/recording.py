import pyaudio
import wave


def record_audio(filename, duration):
    audio = pyaudio.PyAudio()

    # 设置录制参数
    format = pyaudio.paInt16  # 音频格式
    channels = 1  # 声道数
    sample_rate = 16000  # 采样率
    chunk = 1024  # 每次读取的音频数据块大小

    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

    frames = []

    print("Recording...")

    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 保存录音数据到WAV文件
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))


if __name__ == "__main__":
    filename = "output.wav"
    duration = 3  # 录制持续时间（秒）
    record_audio(filename, duration)
