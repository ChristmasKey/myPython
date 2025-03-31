# myPython

![python-logo](./images/python-logo.png)

<h3 style="color:orange;">Python可以干什么？</h3>

<h5 style="color:#ff4c00;">网络爬虫</h5>

<img src="./images/网络爬虫.png" alt="网络爬虫" style="zoom: 50%;" />

<h5 style="color:#c91f37;">网站开发</h5>

<img src="./images/网站开发.png" alt="网站开发" style="zoom: 50%;" />

<h5 style="color:#ff0097;">数据分析</h5>

<img src="./images/数据分析.png" alt="数据分析" style="zoom:50%;" />

<h5 style="color:#f20c00;">自动化办公</h5>

<img src="./images/自动化办公.png" alt="自动化办公" style="zoom:50%;" />



## 安装Python与PyCharm

[Python官网](https://www.python.org)

**1、python解释器：略**

相关命令：

```sh
# 在命令行中启用Python
python

# 查看Python版本
python -V

# 查看Python安装位置
where python
```



**2、pycharm编辑器：略**



## 入门程序

### 1、认识Python

<span style="color:blue;">Python语言</span>是一种<span style="color:red;">面向对象</span>的<span style="color:red;">解释型</span>高级编程语言。

<span style="color:blue;">Python</span>是<span style="color:red;">强类型</span>的<span style="color:red;">动态脚本语言</span>。

> 编译型语言 和 解释型语言
>
> 解释型语言：使用专门的解释器将源码程序逐行解释成特定平台的机器并立即执行，是代码在执行时才被解释器逐行动态翻译和执行，而不是在执行之前就完成翻译。
>
> ![解释型语言](./images/解释型语言.png)
>
> 
>
> 编译型语言：使用专门的编译器，针对特定的平台，将高级语言源代码一次性的编译成可被该平台硬件执行的机器码，并包装成该平台所能识别的可执行程序的格式。
>
> ![编译型语言](./images/编译型语言.png)
>
> <span style="color:red;">区别：</span>
>
> 1.编译型语言编译后就可以在平台运行，解释型语言在运行期间才编译。
>
> 2.一般来说，编译型语言**运行速度**快。
>
> 3.解释型语言**跨平台特性**比编译型语言好。



### 2、HelloWorld

①新建第一个项目

![新建第一个Python项目](./images/新建第一个Python项目.png)

②在项目目录下新建一个hello_world.py文件，并编写如下内容

![新建第一个Python文件](./images/新建第一个Python文件.png)

```python
print("hello world")
```

③在文件空白处点击右键，打开菜单并选择运行文件

![运行第一个Python文件](./images/运行第一个Python文件.png)

可以在控制台查看文件运行结果

![第一个Python文件的运行结果](./images/第一个Python文件的运行结果.png)



### 3、Bug与Debug

Python中常见的Bug类型有：

- 输入错误

```python
print(“123”)    # Python中的符号都要求使用英文符号
```

- 缩进错误

```python
    print("123")    # print要顶格写
```

- 语法错误

```python
print("123")print("456")    # 每个print都必须独占一行
```

- 命名错误

```python
print(hello_world)    # 字符串必须用引号包裹，单引号、双引号都可以
```



Python中设置<span style="color:red;">断点</span>与<span style="color:red;">Debug</span>：

![断点与调试](./images/断点与调试.png)

Debug窗口的一些图标及功能：

![Debug窗口的一些功能图标](./images/Debug窗口的一些功能图标.png)

总结：<span style="color:blue;">可以通过Debug调试看到程序执行的顺序</span>。



### 4、注释

单行注释、多行注释

```python
# 单行注释
print("单行注释")

'''
多行注释（单引号*3）
'''
"""
多行注释（双引号*3）
"""
print("多行注释")

'''
快捷键：
ctrl + /
'''
print("快捷键")
```



### 5、输出函数

```python
# print()方法用于打印输出，是最常见的一个函数
print("123")
```

参数：

- *values：值，表示可以一次输出多个对象。输出多个对象时，需要用英文逗号`,`分隔
- sep：用来间隔多个对象，默认值是一个空格
- end：用来设定以什么结尾，默认值是换行符`\n`，可以换成其他字符串

```python
print("Spring", "is", "coming", sep="_", end="!")
```



### 6、变量

变量的作用：计算机中的存储空间，用于保存数据

```python
# 变量名 = 值
# 注意：赋值运算符 =
num1 = 3
num2 = 10
total = num1 + num2
# 如果变量没有被赋值，则会报命名错误
# 变量只有在被赋值以后才会被创建，所以使用变量之前必须要赋值一次，我们称之为初始化变量
print(num1, num2, total)
```

<span style="color:red;">注意事项：</span>首次使用变量会在内存中划分空间，并初始化值；再次使用变量时不再划分空间，而是修改原空间的值。

```python
# 解释器做了两件事情：
# 1.在内存中创建了一个数据 666
# 2.创建了一个变量a，把666这个数据保存到a变量中去
a = 666
print(a)
# 同一个变量可以反复赋值，并且可以赋值不同的数据类型
a = 999
a = 6.66
a = "哈哈"
print(a)

b = a
print(b)
```



### 7、标识符

http://bilibili.com/video/BV1rpWjevEip/?spm_id_from=333.1391.0.0&p=5&vd_source=71b23ebd2cd9db8c137e17cdd381c618
