"""
函数能够带来最大化的代码重用和最小化的代码冗余。精心设计的函数不仅可以提高程序的健壮性，还可以增强可读性、减少维护成本。先来看以下示例代码：
"""
import smtplib


def httplib():
    pass


def MIMETEXT():
    pass


def SendContent(ServerAdr, PagePath, sender,
                receiver, smtpserver, username, password):
    # 获取网页内容
    http = httplib.Http(ServerAdr)
    http.putrequest('Get', PagePath)
    http.putheader('Accept', 'text/html')
    http.putheader('Accept', 'text/plain')
    http.endheaders()
    httpcode, httpmsg, headers = http.getreply()
    if httpcode != 200:
        return 'error'

    # 查找指定网页内容
    doc = http.getfile()
    data = doc.read()
    doc.close()
    lstr = data.splitlines()
    subject = "Contented get from the web"

    # 发送邮件
    msg = MIMETEXT(lstr)
    msg['Subject'] = subject
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


"""

原则1 函数设计要尽量短小，嵌套层次不宜过深。所谓短小，就是跟前面所提到的一样尽量避免过长函数，
因为这样不需要上下拉动滚动条就能获得整体感观，而不是来回翻动屏幕去寻找某个变量或者某条逻辑判断等。
函数中需要用到if、elif、while、for等循环语句的地方，尽量不要嵌套过深，最好能控制在3层以内。
相信很多人有过这样的经历：为了弄清楚哪段代码属于内部嵌套，哪段属于中间层次的嵌套，
哪段属于更外一层的嵌套所花费的时间比读代码细节所用时间更多。

原则2 函数申明应该做到合理、简单、易于使用。除了函数名能够正确反映其大体功能外，
参数的设计也应该简洁明了，参数个数不宜太多。
参数太多带来的弊端是：调用者需要花费更多的时间去理解每个参数的意思，测试人员需要花费更多的精力来设计测试用例，
以确保参数的组合能够有合理的输出，这使覆盖测试的难度大大增加。因此函数参数设计最好经过深思熟虑。


原则3　函数参数设计应该考虑向下兼容。实际工作中我们可能面临这样的情况：
随着需求的变更和版本的升级，在前一个版本中设计的函数可能需要进行一定的修改才能满足这个版本的要求。
因此在设计过程中除了着眼当前的需求还得考虑向下兼容

原则4 原则4 一个函数只做一件事，尽量保证函数语句粒度的一致性。
如本节开头所示代码中就有3个不同的任务：获取网页内容、查找指定网页内容、发送邮件。
要保证一个函数只做一件事，就要尽量保证抽象层级的一致性，所有的语句尽量在一个粒度上。
如上例既有http.getfile()这样较高层级抽象的语句，也有细粒度的字符处理语句。
同时在一个函数中处理多件事情也不利于代码的重用，在上例中，如果程序中还有类似发送邮件的需求，必然造成代码的冗余。

最后，根据以上几点原则，上面对本节最开始处的代码进行修改，来看看修改后的代码是不是可读性要好一些。
"""


def GetContent(ServerAdr, PagePath):
    # 获取网页内容
    http = httplib.Http(ServerAdr)
    http.putrequest('Get', PagePath)
    http.putheader('Accept', 'text/html')
    http.putheader('Accept', 'text/plain')
    http.endheaders()
    httpcode, httpmsg, headers = http.getreply()
    if httpcode != 200:
        return 'error'

    # 查找指定网页内容
    doc = http.getfile()
    data = doc.read()
    doc.close()
    lstr = data.splitlines()
    return lstr


def SendContent(sender, receiver, smtpserver, username, password, lstr):
    subject = "Contented get from the web"

    # 发送邮件
    msg = MIMETEXT(lstr)
    msg['Subject'] = subject
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

"""
Python中函数设计的好习惯还包括：不要在函数中定义可变对象作为默认值，使用异常替换返回错误，保证通过单元测试等。
"""