# 需要导入copy模块
import copy

# 定义一个嵌套列表list1
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 将list1浅拷贝给list2
list2 = copy.copy(list1)
print("list1", list1)
print("list2", list2)
# 查看list1、list2的内存地址：地址值不同，说明不是同一个对象
print("list1的内存地址", id(list1))
print("list2的内存地址", id(list2))
# 查看list1、list2的嵌套列表的内存地址：地址值相同，说明是同一个对象
print("list1的嵌套列表的内存地址", id(list1[0]))
print("list2的嵌套列表的内存地址", id(list2[0]))
# 给list1添加一个元素后再查看list1、list2的值
list1.append(10)
print("list1", list1)
print("list2", list2)
# 给list2的嵌套列表添加一个元素后再查看list1、list2的值
list2[0].append(11)
print("list1", list1)
print("list2", list2)

# 优点：拷贝速度快、占用空间少、拷贝效率高