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

pygame.key.set_repeat(10, 15)
这两个参数都是以ms为单位的

在pygame中对按键的连续检测是默认失能的，调用上述函数便可以使能按键的连续检测。
按键的连续检测使能后，当按键按下时，将会以delay的延时去触发第一次的KEYDOWN事件，
之后则会以interval的延时去触发接下来的KEYDOWN事件。
通俗的讲，第一个参数影响着按键的灵敏度，第二个参数影响着按键的移动时间间隔

'''

import pygame
from pygame.locals import *
import time   #  如果CPU占用太多，加上sleep
import random

class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/" + image_name)

class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []   # 存储发射出去的子弹对象的引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:  # 多个子弹的循环发射
            bullet.display()
            bullet.move()

class HeroPlane(BasePlane):   #  定义飞机的类
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 200, 700, "hero1.png")   # super().__init__()

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

    def go(self):
        self.y -= 5

    def back(self):
        self.y += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        self.dirction = "right"
        BasePlane.__init__(self, screen_temp, 0, 45, "enemy0.png")   # super().__init__()

        # 存放需要删除的元素
        needDeleteItem = []

        # 判断要删除的子弹
        for i in self.bullet_list:
            if i.judge():  # 判断子弹的越界
                needDeleteItem.append(i)
        # 遍历删除元素
        for j in needDeleteItem:
            self.bullet_list.remove(j)

    def move(self):
        if self.dirction == "right":
            self.x += 5
            self.y += 1
        elif self.dirction == "left":
            self.x -= 5
            self.y += 1

        if self.x > 480 - self.image.get_width():
            self.dirction = "left"
        elif self.x <= 0:
            self.dirction = "right"

    def fire(self):  # 控制频率
        random_num = random.randint(1, 100)
        if random_num in [11, 22]:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class BaseBullet(Base):
    def display(self):  # 显示
        self.screen.blit(self.image, (self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 40, y - 20, "bullet.png")

    def move(self):  # 移动
        self.y -= 5

    def judge(self):    # 判断字段是否删除
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 25, y + 40, "bullet1.png")

    def move(self):  # 移动
        self.y += 4

    def judge(self):    # 判断字段是否删除
        if self.y > 852:
            return True
        else:
            return False

def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            # print("exit")
            exit()
        # 判断是否按下了键
        elif event.type == KEYDOWN:
            pygame.key.set_repeat(10, 100)   # 控制连续按键
            # key_pressed = pygame.key.get_pressed()  # 接受按下键的变量
            # 检测按键是否是a或者left
            # for i in key_pressed:
            #     if i[pygame.K_a] or i[pygame.K_LEFT]:
            if event.key == K_a or event.key == K_LEFT:
                # hero.x -= 20  # 控制移动的像素点
                hero_temp.move_left()
                # print("left")

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                # hero.x += 20
                hero_temp.move_right()
                # print("right")
            elif event.key == K_w or event.key == K_UP:
                hero_temp.go()
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.back()

            # 检测按键是否是空格
            elif event.key == K_SPACE:
                # print("space")
                hero_temp.fire()

        # 判断是否鼠标点击
        elif event.type == MOUSEBUTTONDOWN:
            pos = (x , y) = pygame.mouse.get_pos()  # 获得鼠标的位置信息
            if 0 < max(pos) < 40:
                pass
                # pygame.quit()
                # pygame.time.wait(1000)


def main():
    pygame.init()
    # 设置时钟
    clock = pygame.time.Clock()

    # 1创建窗口,用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")
    # 创建暂停和开始
    # white_background = pygame.image.load("./feiji/white_backgroud.png")
    pause = pygame.image.load("./feiji/game_pause_nor.png")
    start = pygame.image.load("./feiji/game_resume_nor.png")
    # 2创建一个飞机对象
    hero = HeroPlane(screen)

    # 创建一个敌机对象
    enemy = EnemyPlane(screen)

    # 游戏主程序是一个大的死循环
    while True:
        # 设定时钟
        clock.tick(40)
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        screen.blit(pause, (0, 0))
        screen.blit(start, (480 - 38, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()

        # 更新显示的内容
        pygame.display.update()
        # x += 1  # 往右移动
        # y -= 1  # 往前移动
        key_control(hero)


        # time.sleep(0.01)   #  游戏延迟 可以修改成为游戏设定的速度，难度


if __name__ == '__main__':
    main()