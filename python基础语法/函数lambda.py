def test_func(compute1):
    result = compute1(1, 2)
    print(f"类型：{type(compute1)}")
    print(f"结果：{result}")


test_func(lambda x, y: x+y)
