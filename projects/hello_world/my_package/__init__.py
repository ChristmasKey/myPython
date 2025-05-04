print("这是__init.py__文件")
# __init__.py文件的主要作用： 导入这个包内的其他模块
# import my_package.registry as registry
#
# 调用registry模块中的reg函数
# registry.reg('包内__init__.py文件调用')

# 相当于导入列表中定义的模块
__all__ = ['registry']