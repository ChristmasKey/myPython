"""
继承：就是让类和类之间转变为父子关系，子类默认继承父类的属性和方法
继承的语法：class 子类名(父类名):
继承的作用：代码重用，减少代码冗余
继承的分类：单继承，多继承，多层继承
"""
# 单继承
class Person:  # 定义父类
    def eat(self):
        print("吃饭")

    def sleep(self):
        print("睡觉")

class Student(Person):  # 定义子类
    def study(self):
        print("学习")

class Teacher(Person):
    pass

# 创建子类对象
stu = Student()
stu.eat()
stu.sleep()
stu.study()
tch = Teacher()
tch.eat()
tch.sleep()


# 多层继承：继承的传递性会让子类拥有其父类及“爷爷类”的属性和方法
class AA:
    def func1(self):
        print("func1")

class BB(AA):
    def func2(self):
        print("func2")

class CC(BB):
    def func3(self):
        print("func3")

# 创建子类对象
cc = CC()
cc.func1()
cc.func2()
cc.func3()


"""
方法的重写
"""
class Father:
    def work(self):
        print("写代码")
    def fun1(self):
        print("fun1")

class Son1(Father):
    def work(self):  # 方法重写（覆盖父类的方法）
        print("写代码，但是不写注释")

class Son2(Father):
    def work(self):  # 方法重写（扩展父类的方法）
        # 调用父类中的同名方法
        # Father.work(self)
        super().work()
        # super(Son2, self).work()

        super().fun1()  # 通过super()也可以调用父类中的其他方法

        print("写代码，但是不写注释，也不写文档")

# 创建子类对象
son1 = Son1()
son1.work()
son2 = Son2()
son2.work()


"""
多继承：子类可以拥有多个父类，并且具有所有父类的属性和方法
"""
class A:
    def func1(self):
        print("func1")

class B:
    def func2(self):
        print("func2")

class C(A, B):
    def func3(self):
        print("func3")

# 创建子类对象
cc = C()
cc.func1()
cc.func2()
cc.func3()

# 当不同父类中存在同名方法时，调用顺序根据子类括号中父类排序（搜索顺序）确定
class A1:
    def func1(self):
        print("A1.func1")
class B1:
    def func1(self):
        print("B1.func1")

class C1(A1, B1):
    pass

class C2(B1, A1):
    pass

# 创建子类对象
c1 = C1()
c1.func1()  # A1.func1
c2 = C2()
c2.func1()  # B1.func1

"""
方法的搜索顺序：Python3中的内置属性__mro__可以查看方法搜索顺序
"""
print(C1.__mro__)  # (<class '__main__.C1'>, <class '__main__.A1'>, <class '__main__.B1'>, <class 'object'>)
print(C2.__mro__)  # (<class '__main__.C2'>, <class '__main__.B1'>, <class '__main__.A1'>, <class 'object'>)