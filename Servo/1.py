from servo import PCA9685
import servo
import time
import math


pwm1=PCA9685(0X60,False)
pwm1.setPWMFreq(60)
pwm2=PCA9685(0X40,False)
pwm2.setPWMFreq(60)





pwm1.setServoAngleP1(0,50)#l zhou
pwm1.setServoAngleP1(1,-20)#l zhou zhuan
pwm1.setServoAngleP1(2,60)#l dabi zhuan
pwm1.setServoAngleP1(3,90)#l jian zhuan
pwm1.setServoAngleP1(4,90)
pwm1.setServoAngleP1(5,90)
pwm1.setServoAngleP1(6,90)
pwm1.setServoAngleP1(7,90)
pwm1.setServoAngleP1(8,70)
pwm1.setServoAngleP1(9,90)
pwm1.setServoAngleP1(10,80)
pwm1.setServoAngleP1(11,80)
pwm1.setServoAngleP1(12,50)
pwm1.setServoAngleP1(13,90)
pwm1.setServoAngleP1(14,90)
pwm1.setServoAngleP1(15,90)



pwm2.setServoAngleP1(0,90)   
pwm2.setServoAngleP1(1,90)
pwm2.setServoAngleP1(2,90)
pwm2.setServoAngleP1(3,90)
pwm2.setServoAngleP1(4,100)
pwm2.setServoAngleP1(5,90)
pwm2.setServoAngleP1(6,90)
pwm2.setServoAngleP1(7,100)
pwm2.setServoAngleP1(8,70)
pwm2.setServoAngleP1(9,100)
pwm2.setServoAngleP1(10,90)
pwm2.setServoAngleP1(11,90)
pwm2.setServoAngleP1(12,90)
pwm2.setServoAngleP1(13,90)
pwm2.setServoAngleP1(14,90)
pwm2.setServoAngleP1(15,90)

while 1=1:
    pwm1.setServoAngleP1(1,-40)
    time.sleep(1)
    pwm1.setServoAngleP1(1,0)
    time.sleep(1)



