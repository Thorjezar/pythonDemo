# coding=utf-8

'''
搭建页面
'''

import pygame
import time   #  如果CPU占用太多，加上sleep

def main():
    # 1创建窗口,用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    # 3把背景图片放到窗口中显示
    while True:

        # 设定需要显示的背景图
        screen.blit(background, (0, 0))

        # 更新显示的内容
        pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()


