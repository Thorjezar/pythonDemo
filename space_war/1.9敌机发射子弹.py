# coding=utf-8

'''

飞机的面向对象方式

循环删除列表的元素，可能会出现漏删的情况。
a = [11,22,33,44,55,66,77]
所以在for循环中的尽量不要删除自己的元素
for i in a:
    print(i)
    if i == 33:
        a.remove(i)

11
22
33
55
66
77

解决方案：利用新的列表存储删除的元素
然后再利用循环遍历删除
a = [11,22,33,44,55,66,77,88]
for i in a:
    if i == 33 or i ==44:
        b.append(i)

for i in b:
    a.remove(i)




'''

import pygame
from pygame.locals import *
import time   #  如果CPU占用太多，加上sleep
import random

class HeroPlane(object):   #  定义飞机的类
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []   # 存储发射出去的子弹对象的引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:  # 多个子弹的循环发射
            bullet.display()
            bullet.move()
            # 判断子弹越界
            # if bullet.judge():
            #     self.bullet_list.remove(bullet)  这种方法会漏除元素

        # 存放需要删除的元素
        needDeleteItem = []
        for i in self.bullet_list:
            if i.judge():
                needDeleteItem.append(i)
        # 遍历删除元素
        for j in needDeleteItem:
            self.bullet_list.remove(j)


    def move_left(self):
        self.x -= 20

    def move_right(self):
        self.x += 20

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/enemy0.png')
        self.dirction = "right" # 控制方向的变量
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move(self):
        if self.dirction == "right":
            self.x += 5
        elif self.dirction == "left":
            self.x -= 5

        if self.x > 480 - self.image.get_width():
            self.dirction = "left"
        elif self.x <= 0:
            self.dirction = "right"

    def fire(self):  # 控制频率
        random_num = random.randint(1, 100)
        if random_num in [11, 22, 33]:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):  # 显示
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):  # 移动
        self.y -= 5

    def judge(self):    # 判断字段是否删除
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 25    # 往右+
        self.y = y + 40    #往下+
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet1.png")

    def display(self):  # 显示
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):  # 移动
        self.y += 4

    def judge(self):    # 判断字段是否删除
        if self.y < 0:
            return True
        else:
            return False

def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                # hero.x -= 20  # 控制移动的像素点
                hero_temp.move_left()
                print("left")

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                # hero.x += 20
                hero_temp.move_right()
                print("right")

            # 检测按键是否是空格
            elif event.key == K_SPACE:
                print("space")
                hero_temp.fire()

def main():
    # 1创建窗口,用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    # 2创建一个飞机对象
    hero = HeroPlane(screen)

    # 创建一个敌机对象
    enemy = EnemyPlane(screen)

    # 3把背景图片放到窗口中显示
    # 游戏主程序是一个大的死循环
    while True:

        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()

        # 更新显示的内容
        pygame.display.update()
        # x += 1  # 往右移动
        # y -= 1  # 往前移动
        key_control(hero)

        time.sleep(0.01)   #  游戏延迟 可以修改成为游戏设定的速度，难度

if __name__ == '__main__':
    main()