# coding=utf-8

'''
烤地瓜应用

1. 分析“烤地瓜”的属性和方法
示例属性如下:
cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！我们的地瓜开始时时生的
cookedString : 这是字符串；描述地瓜的生熟程度
condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等
示例方法如下:
cook() : 把地瓜烤一段时间
addCondiments() : 给地瓜添加配料
__init__() : 设置默认的属性
__str__() : 让print的结果看起来更好一些

'''

class SweetPotato:

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = [] # 使用列表进行存储多个变量

    def __str__(self):
        return "地瓜 烤的%s(%d) 添加了作料：%s"%(self.cookedString, self.cookedLevel, str(self.condiments))

    def Cooked(self, cookedTime):
        self.cookedLevel += cookedTime # 使用对象属性 来积累烤的时间！ self.cookedLevel 是作为对象的属性来使用的
        if 0<= self.cookedLevel< 3:
            self.cookedString = "生的"
        elif 3<= self.cookedLevel< 5:
            self.cookedString = "半生不熟"
        elif 5<= self.cookedLevel < 8:
            self.cookedString = "熟了"
        else:
            self.cookedString = "烤糊了"

    def addCondiments(self, item):
        self.condiments.append(item)


di_gua = SweetPotato()
di_gua.Cooked(2)
di_gua.addCondiments("番茄酱")
print(di_gua)
di_gua.Cooked(2)
di_gua.addCondiments("芥末")
print(di_gua)
di_gua.Cooked(2)
di_gua.addCondiments("烧烤酱")
print(di_gua)
di_gua.Cooked(2)
print(di_gua)