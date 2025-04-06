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

**开发人员定义的变量名、函数名**

标识符<span style="color:red;">规定</span>：

1. 只能由数字、字母、下划线组成

2. 不能以数字开头

3. 不能是关键字

4. 严格区分大小写

```python
# 定义标识符
six = 1
_six1 = 2
_2six = 3
# 错误写法
# 1_six = 6

# ========================注意项：========================
# Python3支持用中文命名标识符，但是不推荐，不符合代码的规范性
价格 = 1
print(价格)

# 用英文小括号()包裹标识符，对标识符本身没有影响
(user) = 1
print((user))
print(user)
# 错误写法
# (user)name = "ZhangSan"
# print((user)name)
# print(username)
```



<b style="color:green;">命名规范</b>

<span style="color:red;">1.见名知义</span>

<span style="color:red;">2.下划线分割法</span>

<span style="color:red;">3.大驼峰命名法</span>

<span style="color:red;">4.小驼峰命名法</span>

```python
# 下划线分割法
user_name = "Json"
# 大驼峰
UserName = "Json"
# 小驼峰
userName = "Json"
```



### 8、数值类型

![Python中的数值类型](./images/Python中的数值类型.png)

<span style="color:red;">检测数据类型的方法：`type()` 函数</span>

```python
# int 整型（常用）：任意大小的整数
num1 = 1
# num1 = 10000
# num1 = -5
print(type(num1))



# float 浮点型：小数
num2 = 1.5
print(type(num2))



# bool 布尔型（重点）：有两个固定的值 True 和 False，通常用于条件判断
# 注意：True 和 False 必须严格区分大小写
print(True)
# 错误写法：print(true)



# 布尔值可以作为整数参与运算：True = 1，False = 0
print(True + False)
print(True + 1)



# complex 复数型（了解）
# 固定写法：z = a + bj，a是实部，b是虚部，j是虚数单位
print(2 + 3j)
# 虚数单位只能用字母j表示，不区分大小写
print(type(1 + 2j))
print(type(2 + 3J))
# 错误写法：print(4 + 4i)

# 复数的计算
m1 = 1 + 2j
m2 = 2 + 3j
print(m1 + m2)
```



### 9、字符串类型

```python
# 字符串特点：内容被引号包裹，单引号、双引号都可以
name = "Spring Stone"
print(name)
print(type(name))



# 当字符串包含了多行内容时，也可以使用三引号
content = """
line1
line2
line3
"""
print(content)



# 注意：多行注释与多行字符串的区别（多行注释不需要赋值给变量）
difference = """
多行
字符串
"""

"""
多行注释
print("多行注释")
"""

print(difference)
```



#### 字符串常见操作

字符串运算符

![字符串运算符](./images/字符串运算符.png)

```python
# 字符串拼接
print("Py" + "thon")
print("Py", "thon", sep="") # 效果同上

# 重复输出
print("python\r" * 3)

# 索引获取字符串
print("python"[1])

# 切片 包前不包后 [start:stop)
print("python"[1:3])
# 定义一个字符串变量，值为26个英文字母
letters = "abcdefghijklmnopqrstuvwxyz"
# 设置步长，指定切片间隔
print(letters[0:26:2])
print(letters[-1:-27:-2])
print(letters[::-1])
print(letters[:3])
print(letters[3:])
# 运行结果如下
# acegikmoqsuwy
# zxvtrpnljhfdb
# zyxwvutsrqponmlkjihgfedcba
# abc
# defghijklmnopqrstuvwxyz

# 成员运算符
print("py" in "pyhon")
print("pie" in "python")
print("py" not in "pyhon")
print("pie" not in "python")

# 原始字符串
print(r"python\r\t")
```



https://www.bilibili.com/video/BV1rpWjevEip?spm_id_from=333.788.player.switch&vd_source=71b23ebd2cd9db8c137e17cdd381c618&p=13



### 10、格式化输出

#### 占位符

占位符：用来占位的符号

占位符的作用：生成一定格式的字符串

占位符的三种方式：

1.百分号 %

```python
# 单个占位符
name = "Stone"
print("my name is %s" % name)

# 多个占位符
age = 18
print("my name is %s, my age is %d" % (name, age))



# 占位符可以格式化替换内容的长度
# 长度不足的默认补空格（若设置正整数，则空格补在前面；若设置负整数，则空格补在后面）
# 长度超过则按原样输出
num = 123
print("%4d" % num) # 输出结果：_123
content = "aaa"
print("%-4s" % content) # 输出结果：aaa_

# 也可以自定义占位符的格式化补齐内容，例如补0（只适用于开头补0，末尾补0无效）
print("%06d" % num)  # 输出结果：000123



# %f：格式化浮点数，默认格式化成6位小数
a = 1.2
print("%f" % a) # 输出结果：1.200000
b = 1.23
print("%f" % b) # 输出结果：1.230000

# 超出的小数位数遵循四舍五入原则
c = 1.2345678
print("%f" % c) # 输出结果：1.234568

# 也可以自定义设置格式化的小数位数：例如设置4位小数
print("%.4f" % a) # 输出结果：1.2000



# %%：百分号转义
print("输出一个百分号%%" % ())
```

百分号% 格式化输出

|  符号  | 描述                                 |
| :----: | ------------------------------------ |
|   %c   | 格式化字符及其ASCII码                |
| **%s** | 格式化字符串（**常用**）             |
| **%d** | 格式化整数                           |
|   %u   | 格式化无符号整型                     |
|   %o   | 格式化无符号八进制数                 |
|   %x   | 格式化无符号十六进制数               |
|   %X   | 格式化无符号十六进制数（大写）       |
| **%f** | 格式化浮点数字，可指定小数点后的精度 |
|   %e   | 用科学计数法格式化浮点数             |
|   %E   | 作用同上，用科学计数法格式化浮点数   |
|   %g   | %f 和 %e 的简写                      |
|   %G   | %F 和 %E 的简写                      |
|   %p   | 用十六进制数格式化变量的地址         |
| **%%** | 百分号转义                           |



2.format()

```python
print("Hello, {name}! You are {age} years old.".format(name="Alice", age=30))
```

从Python 3.6开始，推荐使用更简洁的 `f-strings` 来格式化字符串。这种方式在性能上通常优于传统的 `format` 方法。



3.格式化 f-strings

```python
# 基本用法
name = "Stone"
age = 18
print(f"my name is {name}, my age is {age}")
```



### 11、运算符

#### 算术运算符

| 运算符 |  描述  |                             实例                             |
| :----: | :----: | :----------------------------------------------------------: |
|   +    |   加   |                         10 + 10 = 20                         |
|   -    |   减   |                         20 - 10 = 10                         |
|   *    |   乘   |                        10 * 10 = 100                         |
|   /    |   除   | 20 / 10 = 2.0（<span style="color:red;">结果一定是浮点数</span>） |
|   //   | 取整除 | 返回商的整数部分，如 9 // 2 = 4（<span style="color:red;">向下取整，无视四舍五入规则，忽略小数</span>） |
|   %    | 取余数 |                    返回余数，如 9 % 2 = 1                    |
|   **   |   幂   |                又称次方、乘方，如 2 ** 3 = 8                 |

<b style="color:red;">注意：式子中如果有浮点数，则结果也会用浮点数表示！</b>

<span style="color:blue;">运算规则：</span>

1.先乘除后加减

2.同级运算符从左往右计算

3.可以用`()`调整计算的优先级

<span style="color:lightgreen;">优先级排序</span>：幂（<span style="color:red;">最高优先级</span>）> 乘、除、取余、取整除 > 加减



#### 赋值运算符

| 运算符 |                       描述                       |          实例          |
| :----: | :----------------------------------------------: | :--------------------: |
|   =    |                 简单的赋值运算符                 |       c = a + b        |
|   +=   |                  加法赋值运算符                  |  c += a 同 c = c + a   |
|   -=   |                  减法赋值运算符                  |  c -= a 同 c = c - a   |
|   *=   |                  乘法赋值运算符                  |  c *= a 同 c = c * a   |
|   /=   |                  除法赋值运算符                  |  c /= a 同 c = c / a   |
|   %=   |  <span style="color:red;">取模</span>赋值运算符  |  c %= a 同 c = c % a   |
|  **=   |                   幂赋值运算符                   | c \**= a 同 c = c ** a |
|  //=   | <span style="color:red;">取整除</span>赋值运算符 | c //= a 同 c = c // a  |

<b style="color:red;">注意：赋值运算符是针对变量存在的，所以不能直接用在计算中！</b>

```python
print(10 += 3) # 错误写法！
```



#### 比较运算符

> ==	!=	>	<	>=	<=



#### 逻辑运算符

> and	or	not



#### 三目运算符

> 为真结果 if 判断条件 else 为假结果

```python
# 基本格式：
num1 = 11
num2 = 3
print("num1更大" if num1 > num2 else "num2更大")
```



### 12、输入函数

`input()`，输入函数，函数的参数是提示词<span style="color:red;">prompt</span>，函数的结果需要定义一个变量去接收。

```python
# 基本使用
name = input("请输入姓名：")
print("你好，" + name + "！")
```



### 13、转义字符

![转义字符](./images/转义字符.png)

Python提供了`r-strings`来取消转义，按字符串内容原样输出：

```python
print(r"Spring\\\tStone") # 输出结果：Spring\\\Stone
```



### 14、if判断

基本写法格式：

```python
# if 要判断的条件:
#     条件成立时执行的代码
age = 18
if age >= 18:
    print("你已经成年了")
```



if-else

```python
score = 60
if score == 100:
    print("good")
else:
    print("not bad")
```



if-elif

```python
score = 60
if score == 100:
    print("perfect")
elif score == 80:
    print("good")
elif score == 60:
    print("not bad")
```



if-elif-else

```python
score = 60
if score == 100:
    print("perfect")
elif score == 60:
    print("good")
else:
    print("work hard")
```



if嵌套

```python
ticket = True
temp = 38.5

if ticket:
    print("有票可以进站")
    # 嵌套了一个 if
    if 36.3 < temp <= 37.2:
        print("体温正常")
    else:
        print("体温异常")
else:
    print("没票不能进站")
```



### 15、循环语句

while循环

```python
# 基本写法：
# 定义初始变量
# while 条件:
#    循环体
#    改变变量
num = 10
while num >= 5:
    print(num)
    num -= 1

# 死循环写法：
while True:
    print("Dead Loop")

# 计算100以内所有整数之和
i = 1
total = 0
while i<= 100:
    total += i
    i += 1
print(total)
```



while循环嵌套（<b style="color:red;">注意：缩进决定层级！！！</b>）

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1
```



for循环

```python
# 基本写法
# for 临时变量 in 可迭代对象:
#     循环体
str = "abcdefg"
for i in str:
    print(i)

# range()函数：包前不包后 [1, 10)
for i in range(1, 10):
    print(i)

# 计算100以内所有整数之和
total = 0
for i in range(1, 101):
    total += i
print(total)
```



> `range()`函数用于生成一个指定范围内的整数序列，可以包含或不包含指定的终止值，并且可以指定步长。
>
> 具体来说，`range(10)`会生成一个从0开始，到9结束的整数序列，即：`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`。
>
> ### 注意事项
>
> 1. `range()`函数生成的序列不包括终止值。例如，`range(10)`生成的序列是`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`，不包括10。
> 2. `range()`函数可以接受三个参数：`range(start, stop, step)`，其中`start`是序列的起始值，`stop`是序列的终止值（不包含），`step`是序列的步长。例如，`range(0, 10, 2)`会生成`[0, 2, 4, 6, 8]`。
> 3. 如果只传入一个参数，如`range(10)`，那么起始值默认为0。
> 4. `range()`函数返回的是一个迭代器对象，而不是一个列表。如果需要列表，可以使用`list()`函数将迭代器转换为列表，例如`list(range(10))`



关键字：break、continue

```python
# break关键字
for i in range(10):
    if i == 5:
        break
    print(i)

# continue关键字
for i in range(10):
    if i == 5:
        continue
    print(i)
```



### 16、字符串编码

![常用编码类型](./images/常用编码类型.png)

字符串编码：本质上就是二进制数据与语言文字的一一对应关系

其中，`Unicode`与`UTF-8`更常用

`Unicode`：所有字符都用2个字节存储，字符与数字之间的转换速度更快，但是占用空间更大；

`UFT-8`：不同的字符用不同的长度存储，更精准，节省了空间，但是字符与数字之间的转换速度较慢，每次都需要计算字符要用多少字节表示。



**字符串编码/解码函数：**

编码`encode()`：将其他编码的字符串转换成`Unicode`编码的字符串

解码`decode()`：将`Unicode`编码的字符串转换成其他编码的字符串

```python
# 字符串类型str是以字符为单位进行处理的
content = "hello"
print(content, type(content))

# 编码content
# 字节类型bytes是以字节为单位进行处理的
encodeContent = content.encode()
print(encodeContent, type(encodeContent))

# 解码encodeContent
decodeContent = encodeContent.decode()
print(decodeContent, type(decodeContent))
```

运行结果如下：

![编码解码函数运行结果](./images/编码解码函数运行结果.png)

其中，第二行结果中的 **b** 表示字节类型结果，对于bytes，只需要知道它和字符串之间的相互转换。

<span style="color:red;">此外，还可以以指定的编码形式对字符串进行编解码操作：</span>

```python
# 以UTF-8格式编码content
content = "社会主义"
encodeContentUtf8 = content.encode('utf-8')
print(encodeContentUtf8, type(encodeContentUtf8))

# 以UTF-8格式解码encodeContentUtf8
decodeContentUtf8 = encodeContentUtf8.decode('utf-8')
print(decodeContentUtf8, type(decodeContentUtf8))
```

