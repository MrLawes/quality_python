"""
Lazy evaluation常被译为“延迟计算”或“惰性计算”，指的是仅仅在真正需要执行的时候才计算表达式的值。
充分利用Lazy evaluation的特性带来的好处主要体现在以下两个方面：
1）避免不必要的计算，带来性能上的提升。对于Python中的条件表达式if x and y，
在x为false的情况下y表达式的值将不再计算。而对于if x or y，
当x的值为true的时候将直接返回，不再计算y的值。因此编程中应该充分利用该特性。

"""

"""
2）节省空间，使得无限循环的数据结构成为可能。Python中最典型的使用延迟计算的例子就是生成器表达式了，它仅在每次需要计算的时候才通过yield产生所需要的元素。
斐波那契数列在Python中实现起来就显得相当简单，而while True也不会导致其他语言中所遇到的无限循环的问题。
"""

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

from itertools import islice
print(list(islice(fib(), 5)))


