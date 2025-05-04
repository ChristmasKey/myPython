"""
闭包：函数嵌套，内部函数引用外部函数的变量，并且外部函数返回内部函数的引用
条件要素：
    1.函数嵌套（函数中再定义函数）
    2.内层函数调用外层函数的局部变量
    3.外层函数的返回值是内层函数的函数名
"""
def outer():        # 外层函数
    a = 10          # 外层函数的局部变量
    def inner():    # 内层函数
        print(a)    # 内层函数调用外层函数的局部变量
    return inner    # 外层函数的返回值是内层函数的函数名

# 调用方式一
outer()()
# 调用方式二
f = outer()
f()

# 带参的闭包函数（外层函数的形参也是它的局部变量）
def param_outer(m):
    n = 10
    def param_inner(o):
        print(m + n + o)
    return param_inner

param_f = param_outer(5)
param_f(20)

# 闭包的原理：函数的引用
def func_a():
    print("func_a")
print(func_a) # 函数名中保存了函数所在位置的引用（内存地址）

# 每次开启内函数都在使用同一份闭包变量
def outer_func(m):
    print("outer_func()函数中的值：", m)
    def inner_func(n):
        print("inner_func()函数中的值：", m, n)
        return m + n
    return inner_func

# 调用外函数，给outer_func()传值
outer_f = outer_func(10)
# 第一次调用内函数
print(outer_f(20))
# 第二次调用内函数
print(outer_f(40))
# 第三次调用内函数
print(outer_f(60))
# 总结：闭包函数可以记录外层函数的变量，并且可以多次调用