"""
装饰器：装饰器本质上是一个闭包函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
"""
# 1.标准版装饰器
def send():
    print('发送邮件')

def outer(fn):  # 外层函数，fn是形参，但是传入的实际值是被装饰的函数名：send
    # 既包含原有功能，又包含新功能
    def inner():  # 内层函数
        print('装饰器开始执行')
        fn()  # 调用被装饰的函数
        print('装饰器结束执行\n')
    return inner

ot = outer(send)
ot()
# 装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包！


# 2.装饰器语法糖
# 格式：@装饰器名
@outer
def funa():
    print('函数funa执行')

funa()

"""
装饰器如何处理被装饰函数的参数：为了处理被装饰函数的参数，装饰器内部通常会定义一个“包装函数”（wrapper function），
这个包装函数会接收任意数量和类型的参数，并在内部调用原始函数。
"""
# 1.标准版装饰器
def send_param(name):
    print('发送邮件给%s' % name)

def outer_param(fn):
    def inner_param(name):
        print('装饰器开始执行')
        fn(name)
        print('装饰器结束执行\n')
    return inner_param

otp = outer_param(send_param)
otp('张三')

# 2.装饰器语法糖
@outer_param
def funb(name):
    print('函数funb执行', name)

funb('李四')

# 3.装饰器处理可变参数和关键字参数
def outer_params(fn):
    def inner_params(*args, **kwargs):
        print('装饰器开始执行')
        fn(*args, **kwargs)
        print('装饰器结束执行\n')
    return inner_params

@outer_params
def func(*args, **kwargs):
    print('函数func执行', args, kwargs)


func('张三', '李四', age=18, sex='男')

"""
多个装饰器：当一个函数被多个装饰器装饰时，所有装饰器是嵌套执行的，由内到外，离函数最近的装饰器先执行，然后外层的装饰器再执行
"""
def outer1(fn):
    def inner1():
        print('装饰器1开始执行')
        fn()
        print('装饰器1结束执行\n')
    return inner1
def outer2(fn):
    def inner2():
        print('装饰器2开始执行')
        fn()
        print('装饰器2结束执行\n')
    return inner2

@outer1
@outer2
def func1():
    print('函数func1执行')

func1()