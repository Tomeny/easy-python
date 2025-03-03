# num1 = 10
# num0 = int(input("请输入第一次猜想的数字："))
# if num1 == num0:
#     print("恭喜你猜对")
# elif num1 != num0:
#     num2 = int(input("不对，再猜一次："))
#     if num2 == num1:
#         print("恭喜你猜对")
#     elif num2 != num1:
#         num3 = int(input("不对，再猜最后一次："))
#         if num2 == num1:
#             print("恭喜你猜对")
#         else:
#             print("Sorry，全部猜错啦，我想的是：10")
num = 5
if int(input("请猜一个数字：")) == num:
    print("恭喜第一次猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry 猜错了")
