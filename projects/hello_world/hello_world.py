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


"""
当全局变量与局部变量命名重复时，全局变量的值并不会被局部变量的值影响而改变
此时应该如何在函数内部修改全局变量的值？
可以使用global关键字，global关键字的作用是：
1.在函数内部声明全局变量
2.在函数内部修改全局变量的值
"""
common_val = 100
print("修改前的全局变量common_val的值：", common_val)


def func4():
    global common_val  # 声明全局变量
    common_val = 200
    print("这是func4中common_val的值：", common_val)


func4()
print("修改后的全局变量common_val的值：", common_val)


def fun5():
    global name
    name = "Python基础"
    print(f"正在学习的课程名称：{name}")


fun5()
print(name)


def fun6():
    print("获取fun5中定义的全局变量的值：", name)


fun6()

# 如何在函数体内部定义多个全局变量