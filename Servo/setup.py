import json
from servo import PCA9685
# 创建一个列表来存储操作的文本表示
operation_history = []

pwm=PCA9685(0x41, debug=False)
pwm.setPWMFreq(50)

class ServoController:
    def __init__(self):
        self.angles = self.load_angles()  # Load angles from file
        self.tight_servo_1=0
        self.tight_servo_2=5

    def save_angles(self):
        '''将当前角度保存到文件中'''
        with open("servo_angles.json", "w") as file:
            json.dump(self.angles, file)

    def load_angles(self):
        '''从文件加载角度'''
        try:
            with open("servo_angles.json", "r") as file:
                angles = json.load(file)
                return {int(k): v for k, v in angles.items()}  # Convert keys to int
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return an empty dictionary if no file exists or if there's an error

    def set_angle(self, servo_number, angle):
        '''设置当前舵机角度并更新文件'''
        if servo_number==(self.tight_servo_1):
            self.angles[servo_number] = angle
            self.angles[servo_number+5] = 180-angle
            print("处理大腿舵机")
            pwm.setServoAngleP1(self.tight_servo_1, angle)
            pwm.setServoAngleP1(self.tight_servo_2, 180-angle)
        else:
            self.angles[servo_number] = angle
            pwm.setServoAngleP1(servo_number, angle)
        self.save_angles()  # Save angles after updating
        self.save_operation(servo_number, angle)
        return angle

    def get_angle(self):
        '''处理用户输入的伺服编号和角度，并设定角度'''
        servo_number = int(input("请输入舵机号："))
        if servo_number in self.angles:
            angle_init = self.angles[servo_number]
            print(f"舵机 {servo_number} 上次设置的角度为 {angle_init}")
        else:
            angle_init = int(input("初始角度:"))

        self.set_angle(servo_number, angle_init)
        self.servo_rotate(servo_number, angle_init)
        return angle_init

    def servo_rotate(self, servo_number, angle_init):
        '''根据用户输入控制舵机转动并决定是否继续'''
        sign = input("向前或向后(前:y,后:n,退出:q):")
        if sign == "y":
            angle = angle_init + int(input("向前转多少度:"))
        elif sign == "n":
            angle = angle_init - int(input("向后转多少度:"))
        elif sign == "q":
            return
        self.set_angle(servo_number, angle)

        flag = input("是否继续(y/n):")
        if flag == "y":
            print("\n")
            self.get_angle()
        else:
            print("结束")
            return

    def get_current_angle(self, servo_number):
        '''Return the current angle of a specified servo'''
        if servo_number in self.angles:
            print("当前舵机号 {} 的角度为 {}".format(servo_number, self.angles[servo_number]))
            return self.angles[servo_number]
        else:
            print("没有找到舵机号为 {} 的舵机记录".format(servo_number))
            return None
        
    def save_operation(self,servo_number, angle):
        if servo_number==(self.tight_servo_1):
            operation1 = f"pwm.setServoAngleP1({self.tight_servo_1}, {angle})"
            operation2 = f"pwm.setServoAngleP1({self.tight_servo_2}, {180-angle})"
            operation_history.append(operation1)
            operation_history.append(operation2)
        else:
            operation = f"pwm.setServoAngleP1({servo_number}, {angle})"
            operation_history.append(operation)


    def print_operation(self):
        # 打印已保存的操作历史
        print("已保存的操作历史：")
        for op in operation_history:
            print(op)

if __name__ == "__main__":
    controller = ServoController()
    controller.get_angle()
    controller.print_operation()
    # Optionally check the angle of a specific servo
    # controller.get_current_angle(0) 