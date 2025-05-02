# 异常处理语法格式一
# 具体异常
a = 1
try:
    print(a)
except NameError as e:
    print('NameError:', e)

# 通用异常
try:
    print(1 / 0)
except Exception as e:
    print('Error')

# 多分支异常
try:
    print(1 / 0)
except NameError as e:
    print('NameError:', e)
except Exception as e:
    print('Error:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)

# 异常处理语法格式二
dict_value = {
    'name': '张三',
}
try:
    print(dict_value["age"])
except Exception as e:
    print('Error:', e)
else:
    print('没有异常')

# 异常处理语法格式三
try:
    print(1 / 0)
except Exception as e:
    print('Error:', e)
finally:
    print('无论是否发生异常，都会执行')

# 异常处理语法格式四
try:
    num = int(input('请输入一个整数:'))
    print(10 / num)
except ValueError as e:
    print('请输入正确的数据')
except Exception as e:
    print('未知错误 %s' % e)
else:
    print('没有异常')
finally:
    print('无论是否发生异常，都会执行')

"""
抛出异常：使用raise语句抛出一个指定的异常
raise [Exception [, args [, traceback]]]
Exception：异常类型，例如：ZeroDivisionError，ValueError等
args：异常参数，字符串类型，如果存在，则必须传入一个参数，如果不存在，则可以不传入参数
traceback：用于跟踪异常的传播路径
"""
def login():
    pwd = str(input("请输入您的密码"))
    if len(pwd) >= 6:
        print('密码输入正确')
    else:
        raise Exception('密码长度不能小于6位')
# 捕捉抛出的异常
try:
    login()
except Exception as e:
    print(e)
print(1234)

# 自定义异常
class AgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return '年龄错误，年龄不能小于18岁，当前年龄为 %s' % self.age


try:
    age = int(input('请输入年龄:'))
    if age < 18:
        raise AgeError(age)
except AgeError as e:
    print(e)
