"""
添加列表元素
append(element)：用于在列表的末尾添加单个元素，该函数会直接修改原列表，而不会返回新的列表；
extend(iterable)：用于将另一个可迭代对象（如列表、元组、字符串等）中的所有元素添加到当前列表的末尾；
注意：
    该函数会直接修改原列表，而不会返回新的列表；
    如果传入的参数不是可迭代对象，会引发TypeError；
    该函数不会添加嵌套的可迭代对象中的元素，而是将整个可迭代对象作为一个单独的元素添加到列表中；
insert(index, element)：用于在列表（list）中插入元素。这个函数可以指定插入的位置，使得新元素插入到列表的指定索引处，而其他元素相应地向后移动；
注意：
    该函数会直接修改原列表，而不会返回新的列表；
    如果指定的索引超出了列表的范围，会引发IndexError；
    如果指定的索引是负数，则表示从列表的末尾开始计数，-1 表示最后一个元素，-2 表示倒数第二个元素，以此类推；
    可以一次性插入多个元素，只需在 element 参数中传入一个可迭代对象（如列表、元组等）；
"""
list1 = [1, 2, 3]
print(list1)
# append()：在列表末尾添加元素
list1.append(4)
print(list1)
# extend()：在列表末尾添加可迭代对象中的所有元素
list1.extend([5, 6])
print(list1)
list1.extend([7, [8, 9]])
print(list1)
# insert()：在列表中插入元素
list1.insert(0, 0)
print(list1)

"""
修改列表元素：直接通过下标进行修改
"""
list2 = [1, 2, 3, 4, 5]
list2[0] = 0
print(list2)

"""
查找列表元素：
in：判断指定元素是否在列表中，如果存在就返回True，否则返回False；
not in：判断指定元素是否存在列表中，如果不存在就返回True，否则返回False；
index()：返回指定元素在列表中第一次出现的索引，如果元素不存在，则引发ValueError；
count()：返回指定元素在列表中出现的次数；
"""
list3 = ["python", "java", "c++", "php", "c#"]
print("python" in list3)
print("c" not in list3)

# 案例：记录用户输入的name，如果重复，提示重复；如果未重复，则添加到列表中
# name_list = []
# while "exit" not in name_list:
#   name = input("请输入姓名：")
#   if name in name_list:
#     print("姓名重复")
#   else:
#     name_list.append(name)
#     print("添加成功")
#     print(name_list)

list4 = ["aa", "bb", "cc", "aa", "dd"]
print(list4.index("dd"))
print(list4.count("aa"))

"""
删除列表元素：
del：删除列表中的指定元素或切片；
pop(index)：删除并返回指定索引处的元素，如果未指定索引，则删除并返回列表中的最后一个元素；
remove(element)：删除列表中第一次出现的指定元素，如果元素不存在，则引发ValueError；
clear()：删除列表中的所有元素；
"""
list5 = ["a", "b", "c", "d"]
del list5[0]  # 根据下标删除元素
del list5[0:2]  # 根据下标范围删除元素
print(list5)
# del list5  # 删除整个列表
# print(list5)  # 报错，list5不存在

list6 = ["a", "b", "c", "d", "e"]
temp1 = list6.pop()  # 默认删除并返回最后一个元素
print(temp1)
print(list6)
temp2 = list6.pop(0)  # 删除并返回指定下标的元素
print(temp2)
print(list6)
# temp3 = list6.pop(9)  # 报错，超出索引范围
# print(temp3)

list7 = ["a", "b", "c", "d", "a"]
list7.remove("a")  # 删除第一个匹配的元素
print(list7)
# list7.remove("z")  # 报错，元素不存在

list7.clear()  # 清空列表
print(list7)  # []

"""
列表元素排序：
sort()：对列表中的元素进行排序，默认是升序排序；
reverse()：反转列表中元素的顺序；
"""
list8 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
list8.sort()
print(list8)
list8.reverse()
print(list8)
# list8.sort(reverse=True)  # 降序排序
# print(list8)

"""
列表推导式：
列表推导式是一种简洁的创建列表的方式，它可以在一行代码中生成一个列表，而不需要使用循环语句。
列表推导式的基本语法是：[expression for item in iterable if condition]
其中，
    expression 是一个表达式，用于生成列表中的元素；item 是可迭代对象中的元素；
    iterable 是一个可迭代对象，如列表、元组、字符串、range()函数等；
    condition 是一个可选的条件表达式，用于筛选满足条件的元素。
"""
nums1 = [1, 2, 3, 4, 5]
[print(i) for i in nums1]  # 列表推导式打印列表中的元素

nums2 = []
# 循环写法
# for i in range(1, 6):
#     nums2.append(i)
# print(nums2)
# 列表推导式写法
[nums2.append(i) for i in range(1, 6)]
print(nums2)

# 将1到10以内的奇数放进nums3列表中
nums3 = []
[nums3.append(i) for i in range(1, 11) if i % 2 != 0]
print(nums3)

"""
列表嵌套：
列表嵌套是指在一个列表中包含另一个列表，即列表中的元素也是列表。
列表嵌套可以用于表示多维数据，如矩阵、二维数组等。
"""
list9 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list9[0])
print(list9[1][2])  # 输出6
# 遍历列表中的每个元素
for i in list9:
    print(i)
# 遍历列表中的每个元素，并输出每个元素中的每个值
for i in list9:
    for j in i:
        print(j)