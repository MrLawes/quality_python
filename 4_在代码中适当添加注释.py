"""
Python中有3种形式的代码注释：块注释、行注释以及文档注释（docstring）。这3种形式的惯用法大概有如下几种

1）使用块或者行注释的时候仅仅注释那些复杂的操作、算法，还有可能别人难以理解的技巧或者不够一目了然的代码。

2）注释和代码隔开一定的距离，同时在块注释之后最好多留几行空白再写代码。下面两行代码显然第一行的阅读性要好。

x = x + 1       # increace x by 1

x = x + 1 # increace x by 1

3）给外部可访问的函数和方法（无论是否简单）添加文档注释。
注释要清楚地描述方法的功能，并对参数、返回值以及可能发生的异常进行说明，使得外部调用它的人员仅仅看docstring就能正确使用。
较为复杂的内部方法也需要进行注释。推荐的函数注释如下：


"""

def func_name(parameter1, parameter2):
    """ Describe what this function does, such as"Find whether the special string is in the queue or not
    :param parameter1: parameter type, what is this parameter used for. such as strqueue: string, string queue list for seach
    :param parameter2: parameter type, what is this parameter used for. such as str: string, string to find

    :return: return type, return value.  such as boolean, sepcial string found return True, else return False
    """
    pass


