""" 建议1：理解Pythonic 概念 """

"""

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

"""
以下几点深入人心：美胜丑，显胜隐，简胜杂，杂胜乱，平胜陡，疏胜密
"""


# 1. 代码风格

# 1.1 两个变量交换
def incorrect_code():
    """ 不正确的示范 """
    a, b = 1, 2
    print(f'a={a},b={b}')
    tmp = a
    a = b
    b = tmp
    print(f'a={a},b={b}')


incorrect_code()


def correct_code():
    """ 正确的示范 """
    a, b = 1, 2
    print(f'a={a},b={b}')
    a, b = b, a
    print(f'a={a},b={b}')


correct_code()


# 1.2 遍历一个数组
def incorrect_code():
    """ 不正确的示范 """
    alist = [1, 2]
    length = len(alist)
    i = 0
    while i < length:
        print(alist[i])
        i += 1


incorrect_code()


def correct_code():
    """ 正确的示范 """
    alist = [1, 2]
    for i in alist:
        print(i)


correct_code()

# 1.3 安全的关闭文件
with open('README.md', 'r') as f:
    print(f.read())


# 1.4 不应当过分的使用奇技淫巧

def incorrect_code():
    """ 不正确的示范 """
    a = [1, 2, 3, 4]
    print(a[::-1])


incorrect_code()

def correct_code():
    """ 正确的示范 """
    a = [1, 2, 3, 4]
    print(list(reversed(a)))


correct_code()
