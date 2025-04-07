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
"""