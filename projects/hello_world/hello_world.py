"""
匿名函数：函数名 = lambda 参数列表：表达式
调用格式：结果 = 函数名(参数列表)
"""
# 1.求两个数的和
# 普通函数
def add(x, y):
    return x + y

print(add(1, 2))

# 匿名函数
# lambda函数不需要写return来返回值，表达式本身结果就是返回值
lambda_add = lambda x, y: x + y
print(lambda_add(1, 2))

"""
匿名函数的参数形式
1.无参数
2.一个参数
3.默认参数
4.可变参数
5.关键字参数
"""
# 1.无参数
no_param = lambda: 100
print(no_param())

# 2.一个参数
one_param = lambda x: x + 1
print(one_param(1))

# 3.默认参数（默认参数必须写在非默认参数后面）
default_param = lambda name, age=18: (name, age)
print(default_param("张三"))
print(default_param("李四", 20))

# 4.可变参数
var_param = lambda *args: args
print(var_param(1, 2, 3, 4, 5))

# 5.关键字参数
key_param = lambda **kwargs: kwargs
print(key_param(name="张三", age=18))