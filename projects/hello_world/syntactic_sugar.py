"""
python中的语法糖：
1.定义大数字
2.交换两个变量值
3.判断变量是否落在某个范围内
4.快速构造字符串
5.列表拼接
6.列表切片
7.打包与解包
8.with语句
9.列表推导式
"""
# 定义大数字
big_num = 10_0000_0000
print(big_num)
# 交换两个变量值
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)
# 判断变量是否落在某个范围内
score = 85
if 80 <= score <= 90:
    print("优秀")
# 快速构造字符串
print("-" * 10)
# 列表拼接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
# 列表切片
list_val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_val[1:3])
print(list_val[5:-2])
# 打包与解包
tuple_val = (1, 2, 3)
x, y, z = tuple_val
print(x, y, z)
temp_tuple = (x, y, z)
print(temp_tuple)
# with语句:with语句用于简化文件操作，自动关闭文件
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
# 列表推导式
list_a = [1, 2, 3, 4]
list_b = [i * 2 for i in list_a]
print(list_b)
set_a = {1, 2, 3, 4}
set_b = { i * 2 for i in set_a}
print(set_b)
dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {k: v * 2 for k, v in dict_a.items()}
print(dict_b)
