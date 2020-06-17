"""
else 在 for；try； while 正常结束的时候执行。
先来看一个没有应用else子句的例子：
"""


def print_prime(n):
    """ 获得质数 """
    for i in range(2, n):
        found = True
        for j in range(2, i):
            if i % j == 0:
                break
        if found:
            print(i, "  is a prime number ")


print_prime(100)

"""
如果对else善加利用，代码可以简洁得多。来看下面的具体实现：
"""


def print_prime2(n):
    """ 获得质数 """
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, "  is a prime number ")


print_prime2(100)

"""
当循环“自然”终结（循环条件为假）时else从句会被执行一次，而当循环是由break语句中断时，else子句就不被执行。
"""

"""
Python的异常处理中有一种try-except-else-finally形式。下面的例子是把数据写入文件中。
"""


def save1():
    try:
        print('save1: 1')
    except:
        print('save1: 2')
    else:
        print('save1: 3')
    finally:
        print('save1: 4')


save1()


def save2():
    try:
        x
    except:
        print('save2: 2')
    else:
        print('save2: 3')
    finally:
        print('save2: 4')

save2()



def save3():
    try:
        print('save3: 1')
    except:
        print('save3: 2')
    else:
        print('save3: 3')
        return 'save3: 3'
    finally:
        print('save3: 4')
        return 'save3: 4'

save3()

