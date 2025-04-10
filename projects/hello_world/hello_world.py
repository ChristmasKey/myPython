"""
集合
"""
set1 = {1, 2, 3}
# 集合与字典都是用{}包裹的，如何区分定义空集合与空字典呢
# 定义空集合必须使用set()函数
set2 = set()
# 定义空字典直接使用{}即可
dict1 = {}
print(set2, type(set2))
print(dict1, type(dict1))

# 集合具有无序性：不能修改集合中的值
set3 = {"a", "b", "c", "d", "e", "f"}
print(set3)  # 集合是无序的，每次输出结果可能不同
set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set3)  # 对于数字元素，每次输出结果都是一样的
# 底层原理涉及hash表
print(hash("a"))
print(hash("b"))
print(hash("c"))
# 每次运行结果都不同，因为字符串的hash值是随机生成的，意味着在hash表中的位置也不同，这也就导致了集合的无序性；（但是同一个字符串的hash值是相同的）
print(hash(1))
print(hash(2))
print(hash(3))
# python中int整型的hash值就是其本身，在hash表中位置是固定的，所以输出结果顺序相同
print(hash("1"))
print(hash("2"))
print(hash("3"))
# 用引号包裹后，整型就变成了字符串类型，所以hash值还是会发生改变

# 集合具有唯一性：集合中不能有重复的元素
set4 = {1, 2, 3, 6, 3, 2, 4}
print(set4)