height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入你的VIP等级（1-5）："))
if height < 120:
    print("身高小于120cm.可以免费")
elif vip_level > 3:
    print("VIP等级大于3.可以免费")
else:
    print("不好意识，条件都不满足，请补票10元")
