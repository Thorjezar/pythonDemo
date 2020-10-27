# coding=utf-8

'''
存放家具应用

目的 把一个对象当做参数 添加到另一个对象中

思维升华：
添加“开、关”灯，让房间、床一起亮、灭

'''
import random

class Home:
    def __init__(self, new_area, new_type, new_addr):
        self.area = new_area
        self.type = new_type
        self.addr = new_addr
        self.left_area = new_area
        self.contain_Items = []
        self.light_Level = 0
        self.light_Statu = "关"

    def __str__(self):
        msg = "房子的总面积是:%d，可用面积是:%d，户型是:%s，地址是:%s"%(self.area, self.left_area, self.type, self.addr)
        msg += "\n房子里面的家具有:%s"%(str(self.contain_Items)) # []列表的转换为字符串 str([])
        msg += "\n房子的灯处于%s ,亮度是%d"%(self.light_Statu, self.light_Level)
        return msg

    def add_item(self, item):
        # self.left_area -= item.area  # 传入床对象的属性
        # self.contain_items.append(item.name) # 传入床的名称属性
        self.left_area -= item.get_Area()
        self.contain_Items.append(item.get_Name())

    def lightList(self,light):  # 灯的状态
        self.light_Level = light.get_Level()
        self.light_Statu = light.get_Statu()


class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area
        self.light_Level = 0
        self.light_Statu = "关"
    def __str__(self):
        return "买了一张%s 床,尺寸是%d，灯光现在处于%s,亮度%d"%(self.name, self.area, self.light_Statu, self.light_Level)

    def get_Area(self):
        return self.area

    def get_Name(self):
        return self.name

    def lightList(self, light):
        self.light_Level = light.get_Level()
        self.light_Statu = light.get_Statu()

class Light:
    def __init__(self):
        self.lightLevel = 0  # 定义亮度 熄灭0~5最亮
        self.lightStatu = "关"

    def __str__(self):
        return "灯的状态是%s,亮度%d"%(self.lightStatu, self.lightLevel)

    def Turn_statu(self):
        if self.lightStatu == "关":
            self.lightStatu = "开"
            self.lightLevel = 1
        elif self.lightStatu == "开" and self.lightLevel <= 5:
            self.lightLevel += 1
        else:
            self.lightStatu = "关"
            self.lightLevel = 0

    def get_Statu(self):
        return self.lightStatu

    def get_Level(self):
        return self.lightLevel

house = Home(130, "三室两厅", "上海市")

bed1 = Bed("席梦思", 4)
bed2 = Bed("乳胶床", 6)
house.add_item(bed2)
house.add_item(bed1)

light = Light()
# light.Turn_statu()  # 操作灯
i = random.randint(1, 10)
j = 0
while j < i:
    light.Turn_statu()
    j += 1


# print(light)
house.lightList(light)
bed1.lightList(light)

print(bed1)
print(house)
