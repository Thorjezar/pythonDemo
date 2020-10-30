# coding=utf-8

'''
虽然子类没有定义__init__方法，但是父类有，所以在子类继承父类的时候这个方法就被继承了，
所以只要创建Bosi的对象，就默认执行了那个继承过来的__init__方法

子类在继承的时候，在定义类时，小括号()中为父类的名字
父类的属性、方法，会被继承给子类

私有的属性，不能通过对象直接访问，但是可以通过方法访问
私有的方法，不能通过对象直接访问
私有的属性、方法，不会被子类继承，也不能被访问
一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用

支持子类继承父类 与 父类的父类

重写：
如果父类中的方法不满足要求，可以在子类中重写方法
名字可以和父类中的方法一模一样的方法

如果要调用父类中被重写的方法
方法一 父类.方法名（self）  *记得加self
方法二 super().方法名()

'''
class Human:
    def __init__(self, name = "人类", color = "黄色"):   # 含有初始化数据的参数，放在最后面
        self.__name = name   # 定义私有属性
        self.color = color

    # 定义父类的方法
    def Eat(self): # 定义方法要带一个参数(self)
        print("吃")

    def Drink(self):
        print("喝")

    def Run(self):
        print("跑")

    def __getName(self): # 定义私有方法
        print(self.__name)

    def getInfo(self):
        print(self.__name, self.color)

class Asia(Human):   # Asia继承 Human
    def Lauguage(self):
        print("汉语")

class Europe(Human):

    def Lauguage(self):
        print("English")

xiaoming = Asia("小明", "黄色")
xiaoming.Lauguage()
xiaoming.getInfo()
xiaoming.Drink()

Ben = Europe("Ben", "White")
# Ben.__getName()
# Europe.__getName()
Ben.Lauguage()
Ben.Run()