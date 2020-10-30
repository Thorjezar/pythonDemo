# coding=utf-8

'''
类方法：
是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，
一般以cls作为第一个参数（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字，
就最好用'cls'了），能够通过实例对象和类对象去访问。

静态方法：
是类中定义的一类没有参数的方法，使用修饰符@staticmethod来标识,
根据实际要求，可以传参，也可以不传参


从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；
而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），
不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。静态方法中不需要额外定义参数，
因此在静态方法中引用类属性的话，必须通过类对象来引用

'''

class Game(object):

    # 类属性
    num = 0

    # 实例方法
    def __init__(self):
        self.name = "laowang"  # 实例属性

    # 类方法 装饰器classmethod
    @classmethod
    def add_num(cls):
        cls.num = 100

    # 定义静态方法
    @staticmethod
    def print_method():
        print("这是个静态方法")

game = Game()
# Game.add_num()  # 通过类名.类方法 直接调用
game.add_num()   # 通过对象名.类方法 调用
print(Game.num)

Game.print_method()   # 通过类名.静态方法名 直接调用
game.print_method()  # 通过对象名.静态方法名 直接调用





