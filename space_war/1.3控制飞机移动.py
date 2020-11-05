# coding=utf-8

'''

控制飞机移动

'''

import pygame
from pygame.locals import *
import time   #  如果CPU占用太多，加上sleep


def main():
    # 1创建窗口,用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    # 2创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")

    x = 200
    y = 700

    # 3把背景图片放到窗口中显示
    while True:

        # 设定需要显示的背景图
        screen.blit(background, (0, 0))

        screen.blit(hero, (x, y))

        # 更新显示的内容
        pygame.display.update()
        # x += 1  # 往右移动
        # y -= 1  # 往前移动

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
                    x -= 20  # 控制移动的像素点
                    print("left")

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 20
                    print("right")



                # 检测按键是否是空格
                elif event.key == K_SPACE:
                    print("space")

        time.sleep(0.01)

if __name__ == '__main__':
    main()