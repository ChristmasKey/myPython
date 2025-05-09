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

# 实例方法和实例属性