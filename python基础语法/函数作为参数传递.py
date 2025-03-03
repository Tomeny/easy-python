def test_func(compute1):
    result = compute1(1, 2)
    print(f"类型：{type(compute1)}")
    print(f"结果：{result}")


def compute(x, y):
    return x+y


test_func(compute)
