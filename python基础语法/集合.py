# 定义集合
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()
print(f"{my_set}的类型是{type(my_set)}")
print(f"{my_set_empty}的类型是{type(my_set_empty)}")
# 添加新元素
my_set.add("python")
my_set.add("传智教育")
print(f"添加后：{my_set}")
# 移除元素
my_set.remove("黑马程序员")
print(f"移除后：{my_set}")
# 随机取出一个元素
my_set = {"传智教育", "黑马程序员", "itheima"}
element = my_set.pop()
print(f"取出元素是:{element}，取出后：{my_set}")
# 清空集合
my_set.clear()
print(f"结果：{my_set}")
# 差集
set1 = {1, 2, 3}
set2 = {1, 4, 6}
set3 = set1.difference(set2)
print(set3)
print(set2)
print(set1)

# 消除差集
set1 = {1, 2, 3}
set2 = {1, 4, 6}
set1.difference_update(set2)
print(set2)
print(set1)

# 合并
set1 = {1, 2, 3}
set2 = {1, 4, 6}
set3 = set1.union(set2)
print(set3)
print(set2)
print(set1)

# 统计
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
num = len(set1)
print(num)
# 遍历
# 集合不支持下标索引， 不能用while循环，可用for循环
