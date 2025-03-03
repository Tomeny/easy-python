import time

count = 0
f = open("/安河桥.txt", "r", encoding="UTF-8")
# 方式1
# for x in f:
#     for n in x:
#         if n == "你":
#             count += 1
#
# print(count)
# f.close()
# 方式2
content = f.read()
count = content.count("你")
print(f"'你'出现的次数：{count}")

