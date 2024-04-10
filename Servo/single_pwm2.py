from servo import PCA9685

# 创建一个列表来存储操作的文本表示
operation_history = []

# 定义一个函数来保存操作


def save_operation(servo, angle):
    operation = f"pwm2.setServoAngleP2({servo}, {angle})"
    operation_history.append(operation)


def print_operation():
    # 打印已保存的操作历史
    print("已保存的操作历史：")
    for op in operation_history:
        print(op)


if __name__ == "__main__":
    pwm2 = PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    while 1:
        servo_input = input("请输入舵机号（输入'q'以停止添加舵机）：")
        if servo_input.lower() == 'q':
            break
        try:
            servo_number = int(servo_input)
            angle = int(input("请输入角度："))
            pwm2.setServoAngleP2(servo_number, angle)
            save_operation(servo_number, angle)
        except ValueError:
            print("输入无效，请确保输入的是有效的数字。")
    # 在循环结束后打印全部结果
    print_operation()
