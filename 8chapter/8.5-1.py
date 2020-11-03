# coding=utf-8

'''
创建文件
捕获异常

'''

import time
import os

# os.mkdir("test")
# os.chdir("./test")

try:
    f = open('demo.txt', 'w')
    f.write("I am YWM\ntesting is a good things\nWe want to talk with you")
    f.close()

    f = open('demo.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        '''
        如果遇到了在读取文件的过程中，产生了异常，那么就会捕捉到
        '''
        pass
    finally:
        f.close()
        print("关闭文档")
except Exception as ret:
    print("没有这个文件")
    print(ret)