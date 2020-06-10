from timeit import Timer
print(Timer("""
x = 1
y = 2
x, y = y, x
""").timeit())



print(Timer("""
x = 1
y = 2
tmp = x
x = y
y = tmp
""").timeit())


import dis

def a():
    x = 1
    y = 2
    x, y = y, x

def b():
    x = 1
    y = 2
    tmp = x
    x = y
    y = tmp

"""
从测试结果可以看出，第二种方式耗费的时间更少，并且由于不需要借助中间变量，
代码更为简洁，是值得推荐的一种方式。那么，为什么第二种方式可以做到更优呢？
这要从Python表达式计算的顺序说起。一般情况下Python表达式的计算顺序是从左到右，
但遇到表达式赋值的时候表达式右边的操作数先于左边的操作数计算，
因此表达式expr3，expr4= expr1，expr2的计算顺序是expr1，expr2→expr3，expr4。
因此对于表达式x，y=y，x，其在内存中执行的顺序如下：1）先计算右边的表达式y，x，
因此先在内存中创建元组（y，x），其标示符和值分别为y、x及其对应的值，其中y和x是在初始化时已经存在于内存中的对象。
2）计算表达式左边的值并进行赋值，元组被依次分配给左边的标示符，通过解压缩（unpacking），元组第一标识符（为y）
分配给左边第一个元素（此时为x），元组第二个标识符（为x）分配给第二个元素（此时为y），
从而达到x、y值交换的目的。更深入一点我们从Python生成的字节码来分析。Python的字节码是一种类似汇编指令的中间语言，
但是一个字节码指令并不是对应一个机器指令。我们通过以下dis模块的来进行分析：
"""


dis.dis(a)
print('#' * 50)
dis.dis(b)

"""
通过字节码可以看出，区别主要集中在swap1函数的第4行和swap2函数的第4～6行代码，
其中swap1的第4行代码对应的字节码中有2个LOAD_FAST指令、2个STORE_FAST指令和1个ROT_TWO指令，
而swap2函数对应的第4～6行代码中共生成了3个LOAD_FAST指令和3个STORE_FAST指令。
而指令ROT_TWO的主要作用是交换两个栈的最顶层元素，它比执行一个LOAD_FAST+STORE_FAST指令更快。
"""