print("第一个自定义模块被调用了")

# 定义变量
name = 'Stone'


def funa():
    print('这是第一个自定义模块的函数')


# 当模块被直接运行时，__name__的值为'__main__'，当模块被其他模块导入时，__name__的值为模块名
if __name__ == 'myModule1':
    print('这是第一个自定义模块的入口')
