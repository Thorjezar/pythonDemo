# coding=utf-8

'''

老王开枪

'''
class Person(object):
    '''人的类'''
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.weapon = None  # 用来保存枪的引用
        self.hp = 100  # 剩余的血量

    def __str__(self):
        if self.weapon:
            return "%s 的血量是%d，持有武器：%s"%(self.name, self.hp, self.weapon)
        else:
            if self.hp > 0:
                return "%s 的血量是%d，他没有武器"%(self.name, self.hp)
            else:
                return "%s 已经阵亡"%self.name

    def load_bullet(self, dan_jia_temp, bullet_temp):
        '''子弹上膛的方法,把子弹押入弹夹中'''
        dan_jia_temp.load_bu(bullet_temp)

    def load_danjia(self, gun_temp, danjia_temp):
        '''枪安装弹夹 枪.安装弹夹(弹夹)'''
        gun_temp.load_danjia(danjia_temp)

    def holdweapon(self, weapon_name):
        '''拿起一把枪'''
        self.weapon = weapon_name

    def koubanji(self, enemy):
        '''让枪发射子弹去打到敌人'''
        self.weapon.openfire(enemy)

    def blood(self, demage):
        '''根据伤害掉相应的血量'''
        self.hp -= demage

class Gun(object):
    '''枪的类'''
    def __init__(self, name):
        super().__init__()
        self.name = name  # 初始化枪的名称
        self.danjia = None  #  初始化弹夹的引用

    def __str__(self):
        if self.danjia:
            return "枪的信息为:%s, 弹夹的信息为:%s"%(self.name, self.danjia)
        else:
            return "枪的信息为:%s" % (self.name)

    def load_danjia(self, danjia_temp):  #  用一个属性保存弹夹
        self.danjia = danjia_temp

    def openfire(self, enemy):
        '''枪从弹夹中获取一发子弹，然后子弹去击中'''
        # 第一个步从弹夹中弹出一颗子弹
        zidan_temp = self.danjia.tanchu_zidan()
        # 第二步子弹击打敌人
        if zidan_temp:
            zidan_temp.onfouce(enemy)
        else:
            print("弹夹中没有子弹了")

class Collection(object):
    '''弹夹的类'''
    def __init__(self, max_num):
        super().__init__()
        self.max_num = max_num   # 用来记录弹夹的最大容量
        self.bullet_list = []  # 用来记录所有的子弹的引用

    def __str__(self):
        return "弹夹的容量为：%d/%d"%(len(self.bullet_list), self.max_num)

    def load_bu(self, zi_dan_temp):  # 将子弹押入弹夹中的方法,用一个属性来保存子弹
        self.bullet_list.append(zi_dan_temp)

    def tanchu_zidan(self):
        '''弹出最上面的一颗子弹'''
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None

class Bullet(object):
    '''子弹的类'''
    def __init__(self, demage):
        super().__init__()
        self.demage = demage

    def onfouce(self, enemy):
        '''打中敌人掉血'''
        enemy.blood(self.demage)

def main():
    '''用来控制流程的主程序'''

    # 1.创建老王对象
    laowang = Person("老王")

    # 2.创建一个枪对象
    ak = Gun("ak47")

    # 3.创建一个弹夹对象
    danjia = Collection(20)

    # 4.创建一些子弹
    for i in range(15):
        bullet = Bullet(10)
        # 6.老王把子弹安装到弹夹中
        laowang.load_bullet(danjia, bullet)
    # 5.创建一个敌人
    gebi_laoli = Person("隔壁老李")

    # 7.老王把弹夹安装到枪中
    laowang.load_danjia(ak, danjia)

    # 8.老王拿枪
    laowang.holdweapon(ak)

    # 9.老王开枪打敌人
    for i in range(12):
        laowang.koubanji(gebi_laoli)
        print(gebi_laoli)
        print(laowang)
    # 测试
    # print(danjia)
    # print(ak)
    # print(laowang)
    # print(gebi_laoli)


if __name__ == '__main__':
    main()