"""
可变类型：变量对应的值可以被修改，但是内存地址不会发生改变
"""
list_val = [1, 2, 3, 4]
print("list_val的原内存地址：", id(list_val))
list_val.append(5)
print("list_val的现内存地址：", id(list_val))
# 数据值改变但是地址值不变，说明是一个可变类型

# 按上面的写法，写一个字典类型的demo
dict_val = {"name": "zhangsan", "age": 18}
print("dict_val的原内存地址：", id(dict_val))
dict_val["sex"] = "male"
print("dict_val的现内存地址：", id(dict_val))

# 按照上面的写法，写一个集合类型的demo
set_val = {1, 2, 3, 4}
print("set_val的原内存地址：", id(set_val))
set_val.add(5)
print("set_val的现内存地址：", id(set_val))

"""
不可变类型：变量对应的值不可以被修改，一旦修改，值的内存地址就会改变（会赋予一个新的值并分配对应的内存空间）
"""
int_val = 10
print("int_val的原内存地址：", id(int_val))
int_val = 20
print("int_val的现内存地址：", id(int_val))
# 数据值改变但是地址值也改变，说明是一个不可变类型

str_val = "hello"
print("str_val的原内存地址：", id(str_val))
str_val = "world"
print("str_val的现内存地址：", id(str_val))

tuple_val = (1, 2, 3, 4)
print("tuple_val的原内存地址：", id(tuple_val))
tuple_val = (5, 6, 7, 8)
print("tuple_val的现内存地址：", id(tuple_val))
