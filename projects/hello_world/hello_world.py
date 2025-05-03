# 模块导入方式一
import modules.myModule1 as myModule1
# 多模块导入
# import modules.myModule1 as myModule1, modules.myModule2 as myModule2

print(myModule1.name)
myModule1.funa()

# 模块导入方式二
from modules.myModule2 import random_num, print_info
print(random_num())
print_info('张三', 18)

# 模块导入方式三
from modules.myModule2 import *
print(random_num())
print_info('李四', 20)