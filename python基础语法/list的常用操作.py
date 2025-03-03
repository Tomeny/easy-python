# 查找某元素的下标索引
mylist = ["itcast", "itheima", "python"]
ihdex = mylist.index("itheima")
print(f"itheima的下标索引是：{ihdex}")
# 修改
mylist[0] = "传智教育"
print(f"修改后的列表：{mylist}")
# 插入
mylist.insert(1, "best")
print(f"插入后：{mylist}")
# 追加
mylist.append("黑马")
print(mylist)
# 多个追加
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(mylist)
# 删除1
del mylist[2]
print(f"删除后：{mylist}")
# 删除2\取出
element = mylist.pop(2)
print(mylist)
print(element)
# 删除某个元素
lists = ["itcast", "itheima", "python", "itheima"]
lists.remove("itheima")
print(lists)
# 清空列表
mylist.clear()
print(f"{mylist}")
# 统计某元素数量
count = lists.count("itheima")
print(f"itheima的数量：{count}")
# 统计全部元素
lists = ["itcast", "itheima", "python", "itheima"]
count = len(lists)
print(f"元素数量：{count}")
