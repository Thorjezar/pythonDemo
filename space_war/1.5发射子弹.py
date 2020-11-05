# coding=utf-8

'''

飞机的面向对象方式

'''

import pygame
from pygame.locals import *
import time   #  如果CPU占用太多，加上sleep

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

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))



class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

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

    # 3把背景图片放到窗口中显示
    while True:

        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        hero.display()

        # 更新显示的内容
        pygame.display.update()
        # x += 1  # 往右移动
        # y -= 1  # 往前移动
        key_control(hero)


        time.sleep(0.01)   #  游戏延迟 可以修改成为游戏设定的速度，难度

if __name__ == '__main__':
    main()