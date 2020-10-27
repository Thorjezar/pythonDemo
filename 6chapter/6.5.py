# coding=utf-8

'''
__init()__方法 被称为魔法方法，具有特殊功能的方法
类初始化的方法

总结1
当创建Car对象后，在没有调用__init__()方法的前提下，BMW就默认拥有了2个属性wheelNum和color，原因是__init__()方法是在创建对象后，就立刻被默认调用了

总结2
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
'''

class Dog:
    def __init__(self):
        print("Ruby is Dog")

dahuang = Dog() # 1.创建一个对象。 2.如果有init方法，调用init方法 3.返回对象的引用给变量

class Cat:
    # 初始化对象
    def __init__(self, skin, age, name):
        if skin == "":
            self.skin = "橙色"
        else:
            self.skin = skin
        if age =="":
            self.age = 10
        else:
            self.age = age
        if name =="":
            self.name = "大脸猫"
        else:
            self.name = name
    '''
    魔法函数 __str__(self)
    
    
    在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
    当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    '''

    def __str__(self):
        return "喵喵的名字:%s\n喵喵的年龄:%d\n喵喵的颜色:%s"%(self.name, self.age, self.skin)  # self 是对象
    # def Miaomiao(self):
    #     print("喵喵的名字:%s\n喵喵的年龄:%d\n喵喵的颜色:%s"%(self.name, self.age, self.skin))

# a = Cat()  报错了，因为初始化没有给出3个对应的参数
b = Cat("红色", 5, "加菲猫")
print(b)
# b.Miaomiao()
