"""

Python提供了3种方式来引入外部模块：import语句、from...import...及__import__函数。
其中较为常见的为前面两种，而__import__函数与import语句类似，
不同点在于前者显式地将模块的名称作为字符串传递并赋值给命名空间的变量。在使用import的时候注意以下几点：
·一般情况下尽量优先使用import a[插图]形式，如访问B时需要使用a.B的形式。·
有节制地使用from a import B形式，可以直接访问B。·尽量避免使用from a import *，
因为这会污染命名空间，并且无法清晰地表示导入了哪些对象。

"""

"""

为什么在使用import的时候要注意以上几点呢？在回答这个问题之前先来简单了解一下Python的import机制。
Python在初始化运行环境的时候会预先加载一批内建模块到内存中，这些模块相关的信息被存放在sys.modules中。
读者导入sys模块后在Python解释器中输入sys.modules.items()便可显示所有预加载模块的相关信息。
当加载一个模块的时候，解释器实际上要完成以下动作：
1）在sys.modules中进行搜索看看该模块是否已经存在，如果存在，则将其导入到当前局部命名空间，加载结束。
2）如果在sys.modules中找不到对应模块的名称，则为需要导入的模块创建一个字典对象，并将该对象信息插入sys.modules中。
3）加载前确认是否需要对模块对应的文件进行编译，如果需要则先进行编译。
4）执行动态加载，在当前模块的命名空间中执行编译后的字节码，并将其中所有的对象放入模块对应的字典中。
我们以用户自定义的模块为例来看看sys.modules和当前局部命名空间发生的变化。
在Python的安装目录下创建一个简单的模块testmodule.py：

"""

import sys
print(dir())
from datetime import MAXYEAR
print(dir())
print(sys.modules['datetime'])
print(id(sys.modules['datetime']))
print(id(MAXYEAR))
# print(id(sys.modules['MAXYEAR']))         # error

"""
了解完import机制，我们再来看看对于from a import ...无节制的使用会带来什么问题。
"""

"""
（1）命名空间的冲突.

来看一个例子。假设有如下3个文件：a.py，b.py及importtest.py，
其中a和b都定义了add()函数，当在import test文件中同时采用from...import...的形式导入add的时候，
import test中起作用的到底是哪一个函数呢？

文件a.py如下:

def add():
    print('add in module A')

文件b.py如下：

def add():
    print('add in model B')
    
文件importtest.py如下：

from a import add
from b import add
add()

从程序的输出“add in module B”可以看出实际起作用的是最近导入的add()，
它完全覆盖了当前命名空间之前从a中导入的add()。
在项目中，特别是大型项目中频繁地使用from a import ...的形式会增加命名空间冲突的概率从而导致出现无法预料的问题。
因此需要有节制地使用from...import语句。一般来说在非常明确不会造成命名冲突的前提下，
以下几种情况下可以考虑使用from...import语句：
1）当只需要导入部分属性或方法时。
2）模块中的这些属性和方法访问频率较高导致使用“模块名.名称”的形式进行访问过于烦琐时。
3）模块的文档明确说明需要使用from...import形式，
导入的是一个包下面的子模块，且使用from...import形式能够更为简单和便利时。
如使用from io.drivers import zip要比使用import io.drivers.zip更方便。

"""

"""
（2）循环嵌套导入的问题先来看下面的例子：
"""

"""
先来看下面的例子：

c1.py:

from c2 import g

def x():
    pass
    
c2.py:

from c1 import x

def g():
    pass

"""

"""
无论运行上面哪一个文件都会抛出ImportError异常。
这是因为在执行c1.py的加载过程中，需要创建新的模块对象c1然后执行c1.py所对应的字节码。
此时遇到语句from c2 import g，而c2在sys.modules也不存在，故此时创建与c2对应的模块对象并执行c2.py所对应的字节码。
当遇到c2中的语句from c1 import x时，由于c1已经存在，于是便去其对应的字典中查找g，
但c1模块对象虽然创建但初始化的过程并未完成，因此其对应的字典中并不存在g对象，此时便抛出ImportError: cannot import name g异常。
而解决循环嵌套导入问题的一个方法是直接使用import语句。读者可以自行验证。

"""

