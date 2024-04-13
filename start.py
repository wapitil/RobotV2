from Offline1_Audio.stt import stt
from Shazzam.main import main
def AudioMode():
    print("进入语音模式")
    result = stt()
    switch = {
        "举双手": case1,
        "前进": case2,
        "后退": case3
    }
    # Using get() with a default case if the command isn't found
    action = switch.get(result, AudioDefault)
    action()

def case1():
    print("举双手")

def case2():
    print("前进")

def case3():
    print("后退")

def AudioDefault():
    # Define what should happen in the default case
    print("未识别指令")
    AudioMode()

def DanceMode():
    '舞蹈模式'
    
def main():
    ''
    result = ""  # 初始化result变量
    while result != "结束表演":
        result = stt()
        if result=="语音模式":
            AudioMode()
        elif result=="舞蹈模式":
            DanceMode()
        print(result)
    
if __name__=="__main__":
    main()
    pass