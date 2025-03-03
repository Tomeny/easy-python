import random
num1 = random.randint(1, 100)
i = 0
flag = True
while flag:
    num2 = int(input("请输入你猜的数字："))
    i += 1
    if num1 > num2:
        print("猜小了")
    elif num1 < num2:
        print("猜大了")
    else:
        print("猜对了")
        flag = False
print(f"总共猜了{i}次")

