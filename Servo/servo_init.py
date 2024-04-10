# from Servo.servo import PCA9685
from servo import PCA9685


def setInitialPosition():
    pwm1 = PCA9685(0x40, debug=False)
    pwm1.setPWMFreq(50)
    pwm1.setServoAngleP1(0, 90)
    pwm1.setServoAngleP1(1, 90)  # 右肩
    pwm1.setServoAngleP1(2, 180)  # 控制上下
    pwm1.setServoAngleP1(3, 90)
    pwm1.setServoAngleP1(4, 90)
    pwm1.setServoAngleP1(5, 180)  # 左键
    pwm1.setServoAngleP1(6, 0)
    pwm1.setServoAngleP1(7, 90)
    pwm1.setServoAngleP1(8, 240)  # 　240 140

    # pwm2 = PCA9685(0x41, debug=False)
    # pwm2.setPWMFreq(50)
    # pwm2.setServoAngleP2(1, 80)
    # pwm2.setServoAngleP2(2, 90)
    # pwm2.setServoAngleP2(3, 105)
    # pwm2.setServoAngleP2(4, 122)
    # pwm2.setServoAngleP2(5, 70)
    # pwm2.setServoAngleP2(6, 90)

    # pwm2.setServoAngleP2(7, 80)
    # pwm2.setServoAngleP2(8, 90)
    # pwm2.setServoAngleP2(9, 105)
    # pwm2.setServoAngleP2(10, 122)
    # pwm2.setServoAngleP2(11, 70)
    # pwm2.setServoAngleP2(12, 90)


if __name__ == "__main__":
    # pwm1 = PCA9685(0x40, debug=False)
    # pwm1.setPWMFreq(50)
    # pwm1.setServoAngleP1(6,0)
    # pwm2 = PCA9685(0x41, debug=False)
    # pwm2.setPWMFreq(50)

    setInitialPosition()
    pass
