def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None


result = check_age(age=int(input("输入年龄：")))
if not None:
    print("未成年！")