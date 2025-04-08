"""
元组：tuple，只支持查询操作，不支持增删改操作；
元组的各个元素的数据类型可以不同；
元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ()，列表使用方括号 []。
"""
tup = (1, 2, 3, 1)
print(type(tup))  # <class 'tuple'>
# 当元组中只有一个元素时，该元素末尾要加一个逗号，否则返回该元素类型的值
tup2 = (1)
print(type(tup2))  # <class 'int'>
tup3 = (1,)
print(type(tup3))  # <class 'tuple'>

print(tup[0])  # 通过下标获取元素
# tup[2] = "a"  # TypeError: 元组不支持修改操作

# 元组的count()、index()、len()函数用法和列表相同
print(tup.count(1))  # 2
print(tup.index(2))  # 1
print(len(tup))  # 4

# 元组同样支持切片操作
print(tup[1:3])  # (2, 3)

"""
应用场景：
1. 不可变类型，如函数的参数，函数的返回值；
2. 格式化输出后面的()本质上就是一个元祖；
3. 数据不可以被修改，保护数据的安全；
"""
name = "张三"
age = 18
print("我叫%s，今年%d岁" % (name, age))
# 简化写法
info = (name, age)
print("我叫%s，今年%d岁" % info)