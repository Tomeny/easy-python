# 局部变量
# def test_a():
#     num = 100
#     print(num)
#
#
# test_a()
# 全局变量
# num = 200
#
#
# def test_a():
#     print(f"test_a:{num}")
#
#
# def test_b():
#     print(f"test_b:{num}")
#
#
# test_a()
# test_b()
# print(num)
# global关键字
num = 200


def test_a():
    print(f"test_a:{num}")


def test_b():
    global num
    num = 1000
    print(f"test_b:{num}")


test_a()
test_b()
print(num)
