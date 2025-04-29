"""
内置函数：
abs()	返回数字的绝对值，如abs(-10) 返回 10

sum()	返回数字序列（元组、列表、集合）的和

min()   返回给定参数的最小值，参数可以为序列；
        参数：min(x, y, z, ..., key=function)；
        比较绝对值大小 min(x, y, key=abs)；

max()   返回给定参数的最大值，参数可以为序列

zip()   拉链函数：将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表

map()   映射函数：将指定的函数依次作用在给定序列的每个元素上，返回一个可迭代对象；
        参数：map(function, iteration)，function为自定义的函数，iteration为可迭代对象；

reduce()
"""
# 查看所有的内置函数（首字母大写的多为内置常量，首字母小写的多为内置函数）
import builtins

print(dir(builtins))

# 拉链函数
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(zip(list1, list2))
# 方式一：通过for循环打印
for i in zip(list1, list2):
    print(i)
    print(type(i))
# 方式二：通过list()函数打印
print(list(zip(list1, list2)))
# 如果元素个数不一致，则按照最短长度匹配元祖

# 映射函数