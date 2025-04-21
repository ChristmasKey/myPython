"""
函数：
定义函数用 def 关键字
函数的返回值用 return 关键字
函数的参数
"""


# 定义函数
def hello_world():
    print("Hello World!")


hello_world()


# 函数的返回值
def fun1():
    print("123")
    return "456"
    # return "456", "789"  # 当return需要返回多个值，会以元组的形式返回
    # return  # 如果函数没有return语句或return没有返回值，函数执行完毕后也会返回结果，只是结果为 None
    # print("789")  # 函数中遇到return语句就会停止执行并返回结果


print(fun1())
