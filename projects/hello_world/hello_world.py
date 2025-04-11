"""
集合的操作：添加元素
add(element)：添加一个元素
update(iterator)：添加多个元素，传入一个或多个可迭代对象，将它们的元素拆分，并逐个放入集合中
"""
set1 = {1, 2, 3}
print("初始集合：", set1)
set1.add(4)
print("添加一个元素后：", set1)
# 当添加重复的元素时，该元素不会被执行任何操作
set1.add(1)
print("添加重复元素后：", set1)

set2 = {1, 2, 3, 4}
print("初始集合：", set2)
set2.update("567")  # 字符串会被拆分成单个字符，并逐个添加到集合中
# set2.update([5, 6, 7])
# set2.update((5, 6, 7))
# set2.update({5, 6, 7})
# set2.update({"name": "张三", "age": 18})  # 集合中默认添加字典的键
print("添加多个元素后：", set2)
# 同样不会添加重复的元素
set2.update({3, 4, 5})
print("添加重复元素后：", set2)
# 传入多个可迭代对象
set2.update("789", [10, 11, 12])
print("添加多个可迭代对象后：", set2)

"""
集合的操作：删除元素
remove(element)：删除指定元素，如果元素不存在，则抛出KeyError异常
discard(element)：删除指定元素，如果元素不存在，则不执行任何操作
pop()：将集合无序排列后的第一个元素删除，并返回该元素（对于int类型集合，排序是固定的，所以pop()函数会永远删除第一个元素）
clear()：清空集合
"""
set3 = {1, 2, 3, 4, 5}
print("初始集合：", set3)

# remove()
set3.remove(3)  # 删除指定元素
print("删除指定元素后：", set3)
# set3.remove(6)  # 删除不存在的元素，抛出KeyError异常
# print("删除不存在的元素后：", set3)

# discard()
set3.discard(4)  # 删除指定元素
print("删除指定元素后：", set3)
set3.discard(6)  # 删除不存在的元素，不执行任何操作
print("删除不存在的元素后：", set3)

# pop()
# int类型集合，pop()函数会永远删除第一个元素
var = set3.pop()
print(var)
print("随机删除一个元素后：", set3)
# str类型集合，pop()函数会将集合无序排列后的第一个元素删除
set4 = {"a", "b", "c", "e", "f"}
print("字符串集合", set4)
var = set4.pop()
print(var)
print("随机删除一个元素后：", set4)

# clear()
set3.clear()  # 清空集合
print("清空集合后：", set3)
# set3.pop()  # 清空集合后，再执行pop()方法，抛出KeyError异常
# print("清空集合后，再执行pop()方法：", set3)

"""
交集：set1 & set2
intersection()：返回两个集合的交集（有返回值）
intersection_update()：返回两个集合的交集，并将结果赋值给调用该方法的集合（直接修改原集合，无返回值）

并集: set1 | set2
union()：返回两个集合的并集
union_update()：返回两个集合的并集，并将结果赋值给调用该方法的集合

差集：set1 - set2
difference()：返回两个集合的差集
difference_update()：返回两个集合的差集，并将结果赋值给调用该方法的集合

对称差集：set1 ^ set2
symmetric_difference()：返回两个集合的对称差集
symmetric_difference_update()：返回两个集合的对称差集，并将结果赋值给调用该方法的集合
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)  # 交集
print(set1 | set2)  # 并集
print(set1 - set2)  # 差集
print(set1 ^ set2)  # 对称差集
print(set1 == set2)  # 判断两个集合是否相等
