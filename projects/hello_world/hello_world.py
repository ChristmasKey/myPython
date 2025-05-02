"""
拆包（unpacking）是一种将一个可迭代对象（如列表、元组、字符串等）中的元素分别赋值给多个变量的操作。
"""
# 列表拆包
numbers = [1, 2, 3]
a, b, c = numbers
print(a)  # 输出：1
print(b)  # 输出：2
print(c)  # 输出：3

# 元组拆包
numbers = (1, 2, 3)
a, b, c = numbers
print(a)  # 输出：1
print(b)  # 输出：2
print(c)  # 输出：3

# 字符串拆包
greeting = "Hello, World!"
first_word, second_word = greeting.split(", ")
print(first_word)  # 输出：Hello
print(second_word)  # 输出：World!

# 字典拆包
person = {"name": "Alice", "age": 25}
name, age = person
print(name)  # 输出：Alice
print(age)  # 输出：25

# 多重拆包
numbers = [1, 2, 3, 4, 5]
*a, b, c = numbers
print(a)  # 输出：[1, 2, 3]
print(b)  # 输出：4
print(c)  # 输出：5
