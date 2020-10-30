# coding=utf-8

'''
游戏规则，1.创建好身份 2.拾取武器 3.进行攻击 4.判断血量为0的阵亡，另一方获胜
1. 人类
属性
姓名
血量
持有的枪
方法
安子弹
安弹夹
拿枪（持有抢）
开枪

2. 子弹类
属性
杀伤力
方法
伤害敌人(让敌人掉血)

3. 弹夹类
属性
容量（子弹存储的最大值）
当前保存的子弹
方法
保存子弹（安装子弹的时候）
弹出子弹（开枪的时候）

4. 枪类
属性
弹夹（默认没有弹夹，需要安装）
方法
连接弹夹（保存弹夹）
射子弹

'''

class Human(object):
    # 类属性
    __blood = 100  # 初始生命值100点血
    __name = "一般人"  # 初始的角色名称
    __fire = "战术军刀"  # 初始角色的武器

    def __init__(self, new_name):
        self.blood = Human.__blood
        self.name = new_name
        self.fire = Human.__fire

    def __del__(self):
        print("角色%s已经阵亡"%self.name)

    def load_bullet(self):
        print("换上子弹")

    def change_clip(self):
        print("安装弹夹")

    def hold_weapon(self):
        print("拿起武器")

    def open_fire(self):
        print("准备开火")

class Bullet(object):
    # 类变量
    __demage = 10  # 固定10点伤害

    @classmethod
    def demage_to_enemy(cls):
        print("造成10点伤害")


class Clip(object):
    # 类变量
    __upload = 10
    __save_bullet = 10

    @classmethod
    def TypeClip(cls, name):
        # 根据传来的枪不同 去设定不同的子弹
        pass

    def load_bullet(self):
        print("子弹上膛")

    def shoot(self):
        print("射出子弹")

class Gun(object):
    __name = "手枪"
    __clip = "手枪弹夹"

    def __init__(self, new_name):
        if new_name == "":
            self.name = Gun.__name
            self.clip = Gun.__clip
        else:
            self.name = new_name
            Bullet


charter = Human("大力")
