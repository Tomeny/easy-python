def list_while_func():
    """
    使用while循环遍历列表
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "python"]
    index = 0
    while index < len(mylist):
        element = mylist[index]
        print(f"{element}")
        index += 1


def list_for_func():
    mylist = [1, 2, 3, 4, 5]
    for x in mylist:
        print(x)


list_for_func()
