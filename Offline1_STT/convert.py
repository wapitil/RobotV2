from pydub import AudioSegment

# 载入MP3文件
audio = AudioSegment.from_mp3("123.mp3")

# 设置新的采样率
audio = audio.set_frame_rate(16000)

# 导出为WAV格式
audio.export("123.wav", format="wav")
