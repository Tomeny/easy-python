# 打开文件
import time

f = open("D:/python/pythonProject4/测试.txt", "r", encoding="UTF-8")
print(type(f))

# 读取文件-read
# print(f"读取10个字节的结果：{f.read(8)}")
# print(f"read方法读取全部内容：{f.read()}")

# 读取文件-readLines()
# lines = f.readlines()
# print(f"Lines对象的类型：{type(lines)}")
# print(f"lines对象的内容：{lines}")

# 读取文件-readLine()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for循环读取文件
# for line in f:
#     print(f"每一行数据是：{line}")
#
# 文件的关闭
# f.close()
# time.sleep(5000)

# with open 语法操作
# with open("D:/python/pythonProject4/测试.txt", "r", encoding="UTF-8") as f:
for line in f:
    print(f"每一行数据是：{line}")
# time.sleep(50000000)
