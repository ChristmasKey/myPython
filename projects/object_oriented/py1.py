"""
类和对象
类的三要素：类名、属性、方法
"""
# 定义类
class WashingMachine:
    height = 800
    width = 600

# 查看类中属性
print(WashingMachine.height)
print(WashingMachine.width)
# 新增类中属性：类名.属性名 = 属性值
WashingMachine.weight = 100
print(WashingMachine.weight)
# 修改类中属性：类名.属性名 = 属性值
WashingMachine.weight = 200
print(WashingMachine.weight)
# 删除类中属性：del 类名.属性名
# del WashingMachine.weight
# print(WashingMachine.weight)

# 创建对象实例（实例化对象）
wm1 = WashingMachine()
print(wm1)  # 默认显示对象的内存地址
wm2 = WashingMachine()
print(wm2)

"""
实例方法和实例属性
实例方法：由对象调用，至少有一个self参数，执行实例方法的时候，自动将调用该方法的对象赋值给self
实例属性：格式 self.属性名
类属性和实例属性的区别：
    类属性：属于类的公共的属性，每个实例对象都能访问到
    实例属性：属于实例对象的私有的属性，只能由对象名进行访问
"""
# 实例方法
class Washer:
    height = 800
    def wash(self):  # self参数是实例方法的必备参数，代表调用该方法的实例本身
        print("洗衣服", self)

wa = Washer()
print(wa)
wa.wash()

# 实例属性
class Person:
    name = "Stone"  # 类属性
    def say_hello(self):  # 实例方法
        print(f"你好，我是{Person.name}，我今年{self.age}岁")

p = Person()
p.age = 18
p.say_hello()

# 通过对象名添加的实例属性，无法通过类名访问，也无法在其他对象中获取
p.sex = "男"
print(p.sex)
# print(Person.sex)  # 报错
p1 = Person()
# print(p1.sex)  # 报错

"""
当我们需要给多个实例对象设置实例属性时，重复上述的属性设置操作比较繁琐，此时可以利用构造函数来处理
构造函数：
"""