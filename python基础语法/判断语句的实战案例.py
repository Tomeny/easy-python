import random
num = random.randint(1, 10)
guss_num = int(input("输入你要猜测的数字："))
if guss_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guss_num > num:
        print("猜大了")
    else:
        print("猜小了")
    guss_num = int(input("再次输入你要猜测的数字："))
    if guss_num == num:
        print("恭喜，第二次就猜中了")
    else:
        if guss_num > num:
            print("猜大了")
        else:
            print("猜小了")
        guss_num = int(input("第三次输入你要猜测的数字："))
        if guss_num == num:
            print("恭喜，第三次就猜中了")
        else:
            print("三次机会已经用完了，没有猜中")
