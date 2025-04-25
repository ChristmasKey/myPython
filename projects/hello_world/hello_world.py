"""
作用域：局部变量、全局变量
"""
# 全局变量
global_val = 100


def func1():
    print("这是func1中global_val的值：", global_val)


def func2():
    global_val = 120
    print("这是func2中global_val的值：", global_val)


print("调用前global_val的值：", global_val)
func1()
func2()
# global_val的值没有被覆盖是因为函数内部如果要使用变量，会先从函数内部寻找，有则直接调用，否则逐层向外寻找。
print("调用后global_val的值：", global_val)


# 局部变量
def func3():
    local_value = "Stone"
    print("这是func3中local_value的值：", local_value)


func3()
# 局部变量的作用：在函数体中临时保存数据，当函数被调用完之后，就会销毁局部变量
# print("这是func3中local_value的值：", local_value)  # NameError: name 'local_value' is not defined
