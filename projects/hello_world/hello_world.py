"""
字典操作：查看元素
1、变量名[键名]
2、变量名.get(键名)
"""
dic1 = {
    "name": "张三",
    "age": 18,
    "gender": "男"
}
print(dic1["name"])
print(dic1.get("age"))
# 二者的区别：当查看的键名不存在时
# print(dic1["address"])  # 报错
# print(dic1.get("address"))  # None
# 自定义键名不存在时，返回的默认值
print(dic1.get("address", "没有这个键"))  # 没有这个键

"""
字典操作：修改元素
变量名[已存在的键名] = 新值
"""
dic1["name"] = "李四"
print(dic1)  # {'name': '李四', 'age': 18, 'gender': '男'}

"""
字典操作：添加元素
变量名[新键名] = 新值 
"""
dic1["address"] = "随机地址"
print(dic1)  # {'name': '李四', 'age': 18, 'gender': '男', 'address': '随机地址'}

"""
字典操作：删除元素
1、del 变量名[键名]
2、变量名.clear()
3、变量名.pop(键名)
"""
dic2 = {
    "name": "张三",
    "age": 18,
    "gender": "男"
}
# 直接删除整个字典变量
# del dic2
# print(dic2) # NameError: name 'dic2' is not defined
# 删除字典中的某个键值对
del dic2["name"]
print(dic2)  # {'age': 18, 'gender': '男'}
# 删除字典中不存在的键值对元素
# del dic2["address"]  # 键名不存在，报错
# print(dic2)

# 清空内容，只留下一个空字典
dic2.clear()
print(dic2)  # {}

# 删除字典中的某个键值对，并返回该键值对的值
dic3 = {
    "name": "张三",
    "age": 18,
    "gender": "男"
}
print(dic3.pop("age"))  # 18
# print(dic3.pop("address"))  # 报错，没有指定键名

# popitem()函数：用于移除并返回字典中的一个键值对
# 3.7之前的版本是随机删除一个键值对，3.7之后的版本默认删除最后一个键值对元素
dic4 = {
    "name": "张三",
    "age": 18,
    "gender": "男"
}
temp = dic4.popitem()
print(temp)  # ('gender', '男')
print(type(temp))  # tuple
print(dic4)

"""
字典操作：求长度（字典中键值对的数量）
len(变量名)
len()函数不仅可以用来计算字典的长度，还可以计算列表、字符串的长度
"""
dic5 = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "tel": "123456"
}
print(len(dic5))  # 4
print(len("hello world"))  # 11
print(len([1, 2, 3, 4, 5]))  # 5

"""
字典操作：获取字典中所有键值对的键名
变量名.keys()
keys()函数返回的是一个视图对象，它是动态的，当字典中的键发生变化，视图对象也会相应地更新
"""
dic5_keys = dic5.keys()
print(dic5_keys)  # dict_keys(['name', 'age', 'gender', 'tel'])
dic5.pop("gender")
print(dic5_keys)  # dict_keys(['name', 'age', 'tel'])
# 将视图对象转换为列表
print(list(dic5_keys))  # ['name', 'age', 'tel']
# 循环打印dic5的所有键名
# 写法1
for key in dic5_keys:
    print(key)
# 写法2
for key in dic5:
    print(key)

"""
字典操作：获取字典中所有键值对的值
变量名.values()
与keys()函数一样，values()函数也返回的是一个动态的视图对象
"""
dic6 = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "tel": "123456"
}
dic6_values = dic6.values()
print(dic6_values)  # dict_values(['张三', 18, '男', '123456'])
dic6["name"] = "李四"
print(dic6_values)  # dict_values(['李四', 18, '男', '123456'])
# 循环打印dic6的所有值
for value in dic6_values:
    print(value)

"""
字典操作：获取字典中所有键值对
变量名.items()
与keys()函数和values()函数一样，items()函数也返回的是一个动态的视图对象，
在这个视图对象中，每个键值对以元组的形式存在
"""
dic7 = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "tel": "123456"
}
dic7_items = dic7.items()
print(dic7_items)  # dict_items([('name', '张三'), ('age', 18), ('gender', '男'), ('tel', '123456')])
# 循环打印dic7的所有键值对
for item in dic7_items:
    print(item, type(item))  # ('name', '张三') <class 'tuple'>
