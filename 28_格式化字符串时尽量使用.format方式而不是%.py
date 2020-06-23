"""

格式化字符串时尽量使用 .format 方式而不是 %

数字格式化

^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。

"""

# 保留小数点后两位, 但是一般不应该用该方式，会导致四舍五入的错误。 >>> 3.14
print('{:.2f}'.format(3.1415926))

# 带符号保留小数点后两位   >>> +3.14   ;  -3.14
print('{:+.2f}'.format(3.1415926))
print('{:+.2f}'.format(-3.1415926))

# 不带小数 >>> 3
print('{:.0f}'.format(3.1415926))

# 数字补零 (填充左边, 宽度为2) >>> 01
print('{:0>2d}'.format(1))

# 数字补x (填充右边, 宽度为4) >>> 1xxx
print('{:x<4d}'.format(1))

# 以逗号分隔的数字格式 >>> 1,000,000
print('{:,}'.format(1000000))

# 百分比格式 >>> 25.00%
print('{:.2%}'.format(0.25))

# 指数记法 >>> 1.00e+09
print('{:.2e}'.format(1000000000))

# 右对齐 (默认, 宽度为10) >>>  '       13'
print('{:>10d}'.format(13))

# 左对齐 (宽度为10)   >>> '13        '
print('{:<10d}'.format(13))

# 中间对齐 (宽度为10)  >>> '    13    '
print('{:^10d}'.format(13))

# 此外我们可以使用大括号 {} 来转义大括号，如下实例
print("{} 对应的位置是 {{0}}".format("runoob"))

"""
.format方法几种常见的用法如下：
"""

# 1）使用位置符号。
print("{0} and {1}".format('a', 'b'))

# 2）使用名称。
print("{a} and {b}".format(a='a', b='b'))


# 3）通过属性。
class User():
    def __init__(self):
        self.name = 'your name'
        self.age = 18
        self.create_at = '2020'


print('{user.name}|{user.age}|{user.create_at}'.format(user=User()))

# 4）格式化元组的具体项。
print('x={0[0]}, y={0[1]}'.format(('x', 'y')))

"""

为什么要尽量使用format方式而不是%操作符来格式化字符串。

理由一：format 方式在使用上较 % 操作符更为灵活。使用format方式时，参数的顺序与格式化的顺序不必完全相同。

理由二：format方式可以方便地作为参数传递。

理由三：%最终会被.format方式所代替。
这个理由可以认为是最直接的原因，根据Python的官方文档（http://docs.python.org/2/library/stdtypes.html#string-formatting），
.format()方法最终会取代%，在Python3.0中.format方法是推荐使用的方法，而之所以仍然保留%操作符是为了保持向后兼容。

"""
