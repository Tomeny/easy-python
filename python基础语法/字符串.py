my_str = "itheima and itcast"
value = my_str[2]
value2 = my_str[-16]
print(f"{value},{value2}")
# index
value = my_str.index("and")
print(f"and的下标：{value}")
# replace
new_my_str = my_str.replace("it", "程序")
print(f"{my_str}替换后:{new_my_str}")
# split
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"{my_str_list}的类型是：{type(my_str_list)}")
# strip
my_str = " itheima and itcast "
new_my_str = my_str.strip()
print(f"{my_str}被strip后，结果是{new_my_str}")
my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(new_my_str)
# count
my_str = "itheima and itcast"
count = my_str.count("it")
# len
print(f"it出现的次数:{count}")
num = len(my_str)
print(num)
