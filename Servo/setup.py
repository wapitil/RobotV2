from servo import PCA9685


def setup():
    ""
    pwm=PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)
    servo_input = input("请输入舵机号（输入'q'以停止添加舵机）：")
    if servo_input.lower() == 'q':
        flag=0
        return flag
    try:
        servo_number = int(servo_input)
        angle = int(input("请输入角度："))
        pwm.setServoAngleP1(servo_number, angle)
        flag=1
        return flag
    except ValueError:
            print("输入无效，请确保输入的是有效的数字。")

if __name__=="__main__":
    flag=1
    while flag:
        flag=setup()