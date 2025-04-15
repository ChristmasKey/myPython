"""
类型转换：int() 将一个数值或字符串转换成整数
"""
val1 = "12"
print(type(val1))
int_val = int(val1)
print(int_val, type(int_val))
# float类型强制转为int类型，会去掉小数部分，只保留整数部分（精度丢失）
print(int(12.84))
# str类型的值中如果有数字和正负号(+/-)以外的字符，在转int类型时会报错
# print(int("abc12"))

# 案例：获取用户从控制台输入的值，并根据该值判断是否成年
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已经成年了")
else:
    print("您还未成年")

"""
类型转换：float() 将一个数值或字符串转换成浮点数
"""
val2 = "12.34"
float_val = float(val2)
print(float_val, type(float_val))
# int类型强制转为float类型，会在后面补上.0
print(float(12))
# str类型的值中如果有数字、小数和正负号(+/-)以外的字符，在转float类型时会报错
# print(float("abc12"))

"""
类型转换：str() 将一个数值转换成字符串
"""
val3 = 100
str_val = str(val3)
print(str_val, type(str_val))
# float类型强制转为str类型时，小数末尾会自动抹零
print(str(12.3400))
# 列表也可以转为str类型
list_val = [1, 2, 3]
print(str(list_val), type(str(list_val)))

"""
类型转换：eval() 将字符串类型的数字或表达式，转成数值类型
"""
# 关于一个计算表达式，以下三种写法的结果是不一样的
print(10 + 10)
print("10" + "10")
print("10+10")
# eval()函数可以将字符串中的表达式进行计算，并返回结果
print(eval("10+10"))
# eval()函数也可以将字符串中的数字转成数值类型
print(eval("10.5"))
# eval()函数也可以实现list、dict、tuple和str类型之间的转换
