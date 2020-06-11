"""
如果你了解JavaScript或者PHP等，那么你一定对eval()所有了解。如果你并没有接触过也没关系，eval()函数的使用非常简单。
"""

print(eval("1+1==2"))
print(eval("'A'+'B'"))
print(eval("1+2"))

"""
Python中eval()函数将字符串str当成有效的表达式来求值并返回计算结果。其函数声明如下：

eval(expression[, globals[, locals]])

其中，参数globals为字典形式，locals为任何映射对象，它们分别表示全局和局部命名空间。
如果传入globals参数的字典中缺少__builtins__的时候，当前的全局命名空间将作为globals参数输入并且在表达式计算之前被解析。
locals参数默认与globals相同，如果两者都省略的话，表达式将在eval()调用的环境中执行。

“eval is evil”（eval是邪恶的），这是一句广为人知的对eval的评价，它主要针对的是eval()的安全性。那么eval存在什么样的安全漏洞呢？来看一个简单的例子：

"""

import sys
from math import *

def ExpCalcBot(string):
    try:
        print("Your answer is", eval(string))
    except:
        print("The expression you enter is not valid")


print("Hi,I am ExpCalcBot. please input your experssion or enter e to end")
while 1:
    print("Please enter a number or operation. Enter c to complete")
    inputstr = input()
    if inputstr == str('e'):
        break
    elif repr(inputstr) != repr(''):
        ExpCalcBot(inputstr)
        inputstr = ""

"""
上面这段代码的主要功能是：根据用户的输入，计算Python表达式的值。它有什么问题呢？
如果用户都是素质良好，没有不良目的的话，那么这段程序也许可以满足基本需求。
比如，输入1+sin(20)会输出结果1.91294525073。但如果它是一个Web页面的后台调用（当然，你需要做一定的修改），
由于网络环境下运行它的用户并非都是可信任的，问题就出现了。因为eval()可以将任何字符串当做表达式求值，
这也就意味着有空子可钻。上面的例子中假设用户输入__import__("os").system("ls")，
会有什么样的输出呢？你会惊讶地发现它会显示当前目录下的所有文件列表.
"""

"""
import("os"). system(del */Q")
!不要轻易在你的计算机上尝试
Your answer is 0
"""

import ast
print(ast.literal_eval('[1 ,2, 3]'))


# def eval_code(code):
#     parsed = ast.parse(code, mode='eval')
#     fixed = ast.fix_missing_locations(parsed)
#     compiled = compile(fixed, '<string>', 'eval')
#     print(eval(compiled))
#
# eval_code("1+sin(20)")
# eval_code('__import__("os").system("ls")')
