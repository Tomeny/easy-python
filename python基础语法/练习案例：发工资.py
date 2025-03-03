import random
num2 = 10000
for x in range(1, 21):
    num1 = random.randint(1, 10)
    if num2 == 0:
        print("工资发完，下个月领取吧。")
        break
    elif num1 < 5:
        print(f"员工{x}，绩效分{num1}，低于5，不发工资下一位。")
    elif num1 >= 5:
        num2 -= 1000
        print(f"向员工{x}发放工资1000元，账户余额还剩余{num2}元。")

