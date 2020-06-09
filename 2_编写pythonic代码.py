"""
（1）要避免劣化代码
"""

"""
    1）避免只用大小写来区分不同的对象。如a是一个数值类型变量，A是String类型，虽然在编码过程中很容易区分二者的含义，
但这样做毫无益处，它不会给其他阅读代码的人带来多少便利。

    2）避免使用容易引起混淆的名称。容易引起混淆的名称的使用情形包括：重复使用已经存在于上下文中的变量名来表示不同的类型；
误用了内建名称来表示其他含义的名称而使之在当前命名空间被屏蔽；没有构建新的数据类型的情况下使用类似于element、list、dict等作为变量名；
使用o（字母O小写的形式，容易与数值0混淆）、l（字母L小写的形式，容易与数值1混淆）等作为变量名。
因此推荐变量名与所要解决的问题域一致。有如下两个示例，示例二比示例一更好。
"""

def incorrect_code(list, num):
    """ 不适当的示范 """
    for element in list:
        if num == element:
            return True


def correct_code(search_list, num):
    """ 正确的示范 """
    for element in search_list:
        if num == element:
            return True


"""
    3）不要害怕过长的变量名。为了使程序更容易理解和阅读，有的时候长变量名是必要的。不要为了少写几个字母而过分缩写。
下例是一个用来保存用户信息的字典结构，变量名person_info比pi的可读性要强得多。
"""


def incorrect_code(list, num):
    """ 不适当的示范 """
    pi = {'name': 'your name'}


def correct_code(search_list, num):
    """ 正确的示范 """
    person_info = {'name': 'your name'}


"""
（2）深入认识Python有助于编写Pythonic代码

接下来介绍风格检查程序PEP8。其实一开始PEP8是一篇关于Python编码风格的指南，
它提出了保持代码一致性的细节要求。它至少包括了对代码布局、注释、命名规范等方面的要求，在代码中遵循这些原则，有利于编写Pythonic的代码。

pip3 install pycodestyle -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com

# 显示每一个错误和警告对应的代码
pycodestyle --show-source --show-pep8 2_编写pythonic代码.py

# 它还可以直接检测一个项目的质量，并通过直观的报表给出报告
pycodestyle --statistics -qq 2_编写pythonic代码.py

PEP8不是唯一的编程规范，事实上，有些公司制定的编程规范也非常有参考意义，比如GooglePython Style Guide。
同样，PEP8也不是唯一的风格检测程序，类似的应用还有Pychecker、Pylint、Pyflakes等。
其中，Pychecker是Google Python Style Guide推荐的工具；
Pylint因可以非常方便地通过编辑配置文件实现公司或团队的风格检测而受到许多人的青睐；
Pyflakes则因为易于集成到vim中，所以使用的人也非常多。

"""

