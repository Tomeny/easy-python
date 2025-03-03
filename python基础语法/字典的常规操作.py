my_dict1 = {"王力宏": 99, "周慧敏": 88, "邓紫棋": 77}
# 新增
my_dict1["周杰伦"] = 100
print(f"新增后:{my_dict1}")
# 更新
my_dict1["周杰伦"] = 50
print(f"更新后:{my_dict1}")
# 删除
num1 = my_dict1.pop("周杰伦")
print(f"结果：{my_dict1},周杰伦的分数：{num1}")
# 清空
my_dict1.clear()
print(my_dict1)
my_dict1 = {"王力宏": 99, "周慧敏": 88, "邓紫棋": 77}
keys = my_dict1.keys()
print(f"keys是：{keys}")
# 遍历
# 方式1
for key in keys:
    print(f"{key}")
    print(f"{my_dict1[key]}")
# 方式2
for key in my_dict1:
    print(f"2.{key}")
    print(f"2.{my_dict1[key]}")
# 统计
num2 = len(my_dict1)
print(num2)
