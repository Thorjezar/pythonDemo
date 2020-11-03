# coding=utf-8

'''
自定义异常处理
引发自定义的异常用 raise

以上程序中，关于代码#super().__init__()的说明
这一行代码，可以调用也可以不调用，建议调用，因为__init__方法往往是用来对创建完的对象进行初始化工作，
如果在子类中重写了父类的__init__方法，即意味着父类中的很多初始化工作没有做，这样就不保证程序的稳定了，
所以在以后的开发中，如果重写了父类的__init__方法，最好是先调用父类的这个方法，然后再添加自己的功能

'''
# 继承了Exception类的自定义异常类
class ShortInputException(Exception):

    def __init__(self, length, atleast):
        super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        i = input("---》")
        if len(i) < 3:
            # 引发自定义的异常
            raise ShortInputException(len(i), 3)
    except ShortInputException as result:
        print("ShortInputException:输入的长度是%d,长度至少应该是%d"%(result.length, result.atleast))
    else:
        print("没有异常发生")

main()

