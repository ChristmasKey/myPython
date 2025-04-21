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


# 函数的参数
# 必备参数（位置参数）：形参和实参的顺序及个数必须一致
def arg_fun1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


arg_fun1("jack", "tom", "lucy")


# 默认参数（缺省参数）：在定义形参时为其设置缺省值，当实参不传值时默认为缺省值
# 格式：def 函数名(参数名=默认值):
# 注意：默认参数必须放在非默认参数后面，无论是函数的定义和调用
def arg_fun2(arg1, arg2="tom", arg3="lucy"):
    print(arg1, arg2, arg3)


arg_fun2("jack", "tom1", "lucy1")
arg_fun2("jack", "tom2")
arg_fun2("jack")


# 可变参数：实参的数量是可变的，可以传入0个或多个
# 格式：def 函数名(*args):
def arg_fun3(*names):
    print(names)
    print(type(names))


arg_fun3("jack", "tom", "lucy")
arg_fun3("jack")
arg_fun3()


# 关键字参数：实参以键值对的形式传入
# 格式：def 函数名(**kwargs):
# 作用：可以扩展函数的功能，如登录接口的选填数据就可以使用关键字参数来接收
def arg_fun4(**kwargs):
    print(kwargs)
    print(type(kwargs))  # 以字典形式接收参数


arg_fun4(name1="jack", name2="tom", name3="lucy")  # 传值的时候，需要采用“键=值”的形式
arg_fun4(name1="jack")
arg_fun4()  # 空字典
