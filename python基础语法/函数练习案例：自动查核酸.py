def temp(x):
    print("欢迎来到黑马程序员！请出示您的健康码，并测量体温！")
    if x <= 37.5:
        print(f"您的体温是：{x}，体温正常请进！")
    else:
        print(f"您的体温是：{x}，需要隔离！")


temp(x=float(input()))
