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

dis.dis(a)
print('#' * 50)
dis.dis(b)

"""
通过字节码可以看出，区别主要集中在swap1函数的第4行和swap2函数的第4～6行代码，
其中swap1的第4行代码对应的字节码中有2个LOAD_FAST指令、2个STORE_FAST指令和1个ROT_TWO指令，
而swap2函数对应的第4～6行代码中共生成了3个LOAD_FAST指令和3个STORE_FAST指令。
而指令ROT_TWO的主要作用是交换两个栈的最顶层元素，它比执行一个LOAD_FAST+STORE_FAST指令更快。
"""