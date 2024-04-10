import time
import math
from smbus2 import SMBus

# 16通道PWM舵机驱动板，使用PCA9685芯片，可控制16路舵机


class PCA9685:

    # Registers/etc.
    __SUBADR1 = 0x02
    __SUBADR2 = 0x03
    __SUBADR3 = 0x04
    __MODE1 = 0x00
    __PRESCALE = 0xFE
    __LED0_ON_L = 0x06
    __LED0_ON_H = 0x07
    __LED0_OFF_L = 0x08
    __LED0_OFF_H = 0x09
    __ALLLED_ON_L = 0xFA
    __ALLLED_ON_H = 0xFB
    __ALLLED_OFF_L = 0xFC
    __ALLLED_OFF_H = 0xFD

    def __init__(self, address=0x40, debug=False):
        "初始化一个PCA9685对象"
        self.bus = SMBus(1)
        self.address = address
        self.debug = debug
        if (self.debug):
            print("Reseting PCA9685")
        # 向PCA9685设备的__MODE1寄存器写入值0x00，以完成PCA9685设备的复位操作
        self.write(self.__MODE1, 0x00)

    def write(self, reg, value):
        "用于向指定的寄存器(或地址)写入一个8位的数值"
        self.bus.write_byte_data(self.address, reg, value)
        if (self.debug):
            print("I2C: Write 0x%02X to register 0x%02X" % (value, reg))

    def read(self, reg):
        "Read an unsigned byte from the I2C device"
        result = self.bus.read_byte_data(self.address, reg)
        if (self.debug):  # 开启调试模式,显示写入的数值和寄存器地址.%02X 是一个格式化字符串，表示按照16进制格式输出数值
            print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" %
                  (self.address, result & 0xFF, reg))
        return result

    def setPWMFreq(self, freq):
        "设置PWM频率"
        prescaleval = 25000000.0    # 25MHz
        prescaleval /= 4096.0       # 12-bit
        prescaleval /= float(freq)
        prescaleval -= 1.0
        if (self.debug):
            print("Setting PWM frequency to %d Hz" % freq)
            print("Estimated pre-scale: %d" % prescaleval)
        prescale = math.floor(prescaleval + 0.5)
        if (self.debug):
            print("Final pre-scale: %d" % prescale)
        oldmode = self.read(self.__MODE1)
        newmode = (oldmode & 0x7F) | 0x10        # sleep
        self.write(self.__MODE1, newmode)        # go to sleep
        self.write(self.__PRESCALE, int(math.floor(prescale)))
        self.write(self.__MODE1, oldmode)
        time.sleep(0.005)
        self.write(self.__MODE1, oldmode | 0x80)

    def setPWM(self, channel, on, off):
        "Sets a single PWM channel"
        # print('pulse:',off)
        self.write(self.__LED0_ON_L+4*channel, on & 0xFF)
        self.write(self.__LED0_ON_H+4*channel, on >> 8)
        self.write(self.__LED0_OFF_L+4*channel, off & 0xFF)
        self.write(self.__LED0_OFF_H+4*channel, off >> 8)
        if (self.debug):
            print("channel: %d  LED_ON: %d LED_OFF: %d" % (channel, on, off))

    def setServoPulse(self, channel, pulse):
        "Sets the Servo Pulse,The PWM frequency must be 50HZ"
        # PWM frequency is 50HZ,the period is 20000us
        pulse = math.floor(pulse*4096/20000)
        self.setPWM(channel, 0, pulse)

    def setServoAngleP1(self, channel, angle):
        "设置舵机的角度"
        if channel == 1 or channel == 8:
            self.setServoPulse(channel, 500+(2000/270)*angle)
        elif channel == 5 or channel == 2:
            self.setServoPulse(channel, 500+(2000/270)*angle)
        else:
            self.setServoPulse(channel, 500+(2000/180)*angle)

    def setServoAngleP2(self, channel, angle):
        "设置舵机的角度"
        self.setServoPulse(channel, 500+(2000/270)*angle)
