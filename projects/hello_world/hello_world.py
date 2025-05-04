# 导入包的方式一
# import my_package
# # 调用包下的registry模块中的reg()函数
# my_package.registry.reg('导入包后调用')

# 导入包的方式二
# from my_package import registry
# # 调用包下的registry模块中的reg()函数
# registry.reg('导入包后调用')

# 导入包的方式三
from my_package import *
# 调用包下的registry模块中的reg()函数
registry.reg('导入包后调用')
# 无法调用login模块中的login()函数
# login.login()