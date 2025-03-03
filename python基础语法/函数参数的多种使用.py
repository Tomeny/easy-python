def user_info(name, age, gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


# 位置参数
user_info('小明', 20, '男')
# 关键字参数
user_info(name='小碗', age=11, gender='女')
user_info(age=10, gender='女', name='小柔')
user_info('甜甜', gender='女', age='10')


# 缺省参数
def user_info(name, age, gender='男'):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


user_info('小天', '18',)
user_info('悠悠', '20', '女')


# 不定长——位置不定长 *号，元组
def user_info(*args):
    print(f"args的内容是：{args},类型：{type(args)}")


user_info(1, 2, 3, 4, '小美', '女孩')


# 不定长——关键字不定长 **号，字典
def user_info(**kwargs):
    print(f"args的内容是：{kwargs},类型：{type(kwargs)}")


user_info(name='小王', age=18, gender='男人')
