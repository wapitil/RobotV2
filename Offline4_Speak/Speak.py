import os
import threading


def play_audio(audio_file, volume=150):
    command = [
        '/usr/bin/mplayer',
        '-ao', 'alsa',
        '-volume', str(volume),  # 将音量值转换为字符串
        audio_file
    ]
    try:
        os.system(' '.join(command))
    except Exception as e:
        print("Error playing audio:", e)


def opening():
    # 请选择表演模式。
    audio_file = "/home/pi/Desktop/Robot/Audio/OpenTip.mp3"
    play_audio(audio_file)


def middle():
    # 请 下达指令。
    audio_file = "/home/pi/Desktop/Robot/Audio/MiddleTip.mp3"
    play_audio(audio_file)


def ending():
    # 表演结束，感谢您的观看。
    audio_file = "/home/pi/Desktop/Robot/Audio/EndTip.mp3"
    play_audio(audio_file)

# 以下为 语音模式所有播报 #


def voice_mode():
    # 切换为语音模式。
    audio_file = "/home/pi/Desktop/Robot/Audio/VoiceMode.mp3"
    play_audio(audio_file)


def lift_lefthand():
    # 举 左手。
    audio_file = "/home/pi/Desktop/Robot/Audio/LiftLeftHand.mp3"
    play_audio(audio_file)


def lift_hands():
    # 举 双手。
    audio_file = "/home/pi/Desktop/Robot/Audio/LiftHands.mp3"
    play_audio(audio_file)


def forword():
    # 前进。
    audio_file = "/home/pi/Desktop/Robot/Audio/Forword.mp3"
    play_audio(audio_file)


def backword():
    # 后退。
    audio_file = "/home/pi/Desktop/Robot/Audio/Backword.mp3"
    play_audio(audio_file)


def move_left():
    # 左 移。
    audio_file = "/home/pi/Desktop/Robot/Audio/MoveLeft.mp3"
    play_audio(audio_file)


def move_right():
    # 右 移。
    audio_file = "/home/pi/Desktop/Robot/Audio/MoveRight.mp3"
    play_audio(audio_file)


def turn_left():
    # 向 左转。
    audio_file = "/home/pi/Desktop/Robot/Audio/TurnLeft.mp3"
    play_audio(audio_file)


def turn_right():
    # 向 右转。
    audio_file = "/home/pi/Desktop/Robot/Audio/TurnRight.mp3"
    play_audio(audio_file)


def single_legged_support():
    # 单脚撑。
    audio_file = "/home/pi/Desktop/Robot/Audio/SingleLeggedSupport.mp3"
    play_audio(audio_file)


# 三个自选动作语音播放 #


def bend_over():
    # 双手叉腰。
    audio_file = "/home/pi/Desktop/Robot/Audio/BendOver.mp3"
    play_audio(audio_file)


def right_angle():
    # 直角展开
    audio_file = "/home/pi/Desktop/Robot/Audio/RightAngle.mp3"
    play_audio(audio_file)


def lunge():
    # 弓箭步
    audio_file = "/home/pi/Desktop/Robot/Audio/Lunge.mp3"
    play_audio(audio_file)


# 以下为 视觉模式提示词 #


def vision_mode():
    # 切换为视觉模式。
    audio_file = "/home/pi/Desktop/Robot/Audio/VisionMode.mp3"
    play_audio(audio_file)


def camera_init():
    # 相机初始化完成，开始检测。
    audio_file = "/home/pi/Desktop/Robot/Audio/CameraInit.mp3"
    play_audio(audio_file)


def action_one():
    # 动作编号一
    audio_file = "/home/pi/Desktop/Robot/Audio/ActionOne.mp3"
    play_audio(audio_file)


def action_two():
    # 动作编号二
    audio_file = "/home/pi/Desktop/Robot/Audio/ActionTwo.mp3"
    play_audio(audio_file)


def action_three():
    # 动作编号三
    audio_file = "/home/pi/Desktop/Robot/Audio/ActionThree.mp3"
    play_audio(audio_file)


def action_four():
    # 动作编号四
    audio_file = "/home/pi/Desktop/Robot/Audio/ActionFour.mp3"
    play_audio(audio_file)


def action_five():
    # 动作编号五
    audio_file = "/home/pi/Desktop/Robot/Audio/ActionFive.mp3"
    play_audio(audio_file)


def action_six():
    # 动作编号五
    audio_file = "/home/pi/Desktop/Robot/Audio/ActionSix.mp3"
    play_audio(audio_file)


# 以下为舞蹈模式提示词 #


def dance_mode():
    # 切换为舞蹈模式。
    audio_file = "/home/pi/Desktop/Robot/Audio/DanceMode.mp3"
    play_audio(audio_file)


def begin_show():
    # 开始表演，三 二 一。
    audio_file = "/home/pi/Desktop/Robot/Audio/BeginShow.mp3"
    play_audio(audio_file)


def song_tip():
    # 请 播放第一首音乐。
    audio_file = "/home/pi/Desktop/Robot/Audio/SongTip.mp3"
    play_audio(audio_file)


def music_one():
    # 音乐编号一
    audio_file = "/home/pi/Desktop/Robot/Audio/MusicOne.mp3"
    play_audio(audio_file)


def music_two():
    # 音乐编号二
    audio_file = "/home/pi/Desktop/Robot/Audio/MusicTwo.mp3"
    play_audio(audio_file)


def music_three():
    # 音乐编号三
    audio_file = "/home/pi/Desktop/Robot/Audio/MusicThree.mp3"
    play_audio(audio_file)


def music_four():
    # 音乐编号四
    audio_file = "/home/pi/Desktop/Robot/Audio/MusicFour.mp3"
    play_audio(audio_file)


def music_five():
    # 音乐编号五
    audio_file = "/home/pi/Desktop/Robot/Audio/MusicFive.mp3"
    play_audio(audio_file)


def song_success():
    # 识别成功，请播放 下一首音乐。
    audio_file = "/home/pi/Desktop/Robot/Audio/SongSuccess.mp3"
    play_audio(audio_file)


def song_fail():
    # 识别失败，请重新播放音乐。
    audio_file = "/home/pi/Desktop/Robot/Audio/SongFail.mp3"
    play_audio(audio_file)
