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
print(temp)
print(dic4)
