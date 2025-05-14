"""
面向对象的三大特性：封装、继承、多态
封装：指的是隐藏对象中一些不希望被外部访问到的属性或者方法

私有属性/方法：只允许在类的内部访问，无法通过对象访问
格式：在属性名或方法名前面加上两个下划线
私有属性不会继承给子类，要访问只能通过间接的方式，另一个py文件中无法通过 from xxx import * 导入
"""
class Person:
    name = "James"
    __age = 18
    def fun1(self):
        Person.__age = 24
        print(f"在实例方法中访问类属性 {Person.name} 和私有属性 {Person.__age}")


p1 = Person()
print(p1.name)
# print(p1.__age)  # 报错

# 如何在外部访问私有属性
# 方式一：需要使用_类名__属性名（仅做了解，尽量不要这么使用）
print(p1._Person__age)
p1._Person__age = 20  # 修改私有属性
print(p1._Person__age)
# 方式二：在类中定义一个方法，用来获取私有属性（正规方式，推荐使用）
p1.fun1()

# 私有方法
class Man:
    def __play(self):
        print("这是一个私有方法 play")
    def fun2(self):
        # Man.__play(self)  # 调用私有方法（不推荐）
        self.__play()  # 调用私有方法
        print("这是一个实例方法")

man = Man()
man.fun2()
# man.__play()  # 报错
# 访问私有方法的两种方法：
# 方式一：通过_类名__方法名（仅做了解，尽量不要这么使用）
man._Man__play()
# 方式二：在类中定义一个方法，用来调用私有方法（正规方式，推荐使用）
man.fun2()

"""
隐藏属性/方法：如果定义在类中，外部可以直接访问
格式：在属性名或方法名前面加上一个下划线
隐藏属性可以继承给子类，另一个py文件中同样无法通过 from xxx import * 导入
"""
class Human:
    name = "Tom"
    __age = 28  # 私有属性
    _sex = "male"  # 隐藏属性

h1 = Human()
# 访问隐藏属性
print(h1._sex)

# 隐藏方法
class Woman:
    def _buy(self):
        print("这是一个隐藏方法 buy")

woman = Woman()
woman._buy()  # 调用隐藏方法