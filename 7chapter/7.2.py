# coding=utf-8

'''
隐藏类的属性
使用set get方法去实现


Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，
否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。

'''

class Demo:
    # 私有方法，举例企业发送短信
    def __send_Msg(self):
        print("=" * 8 + "正在发送短信" + "=" * 8)

    def send_Msg(self, money):
        if money > 10000:
            self.__send_Msg()   # 定义私有方法的目的是，可以先调用公有方法进行验证，然后再调用核心的私有方法
        else:
            print("余额不足，请及时充值")

demo = Demo()
demo.send_Msg(1000)