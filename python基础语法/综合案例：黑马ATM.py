# myself
# money = 50000000
# name = input("请输入名字")
#
#
# def find():
#     print(f"您的余额为{money}")
#
#
# def save():
#     save_money = int(input("请输入存入金额："))
#     global money
#     print(f"目前余额为：{money + save_money}")
#
#
# def get():
#     get_money = int(input("请输入取出金额："))
#     global money
#     print(f"目前余额为：{money + get_money}")
#
#
# def menu():
#     print("1.查询余额\t")
#     print("2.存款\t")
#     print("3.取款\t")
#     print("4.退出\t")
#     print("(请输入1-4)")
#     num = int(input())
#     if num == 1:
#         find()
#     elif num == 2:
#         save()
#
#     elif num == 3:
#         get()
#     else:
#         exit()
#
#
# menu()


# other

money = 50000000
name = input("请输入您的名字")


def query(show):
    if show:
        print("-------查询余额--------")
    print(f"{name}，您好，您的余额剩余：{money}")


def saving(num):
    global money
    money += num
    print("-------存款-------")
    print(f"{name}，您好，您存款{num}元成功")
    query(False)


def get_money(num):
    global money
    money -= num
    print("-------取款-------")
    print(f"{name}，您好，您取款{num}元成功。")
    query(False)


def main():
    print("-------主菜单-------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作。")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入您的选择："))


while True:
    key = main()
    if key == 1:
        query(True)
        continue
    elif key == 2:
        num1 = int(input("请输入存款金额："))
        saving(num1)
        continue
    elif key == 3:
        num2 = int(input("请输入取款金额："))
        get_money(num2)
        continue
    else:
        print("退出成功！")
        break
