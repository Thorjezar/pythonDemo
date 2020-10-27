# coding=utf-8

'''
2. 制作一个"密码薄",其可以存储一个网址（例如 www.itcast.cn），和一个密码(例如 123456)，请编写程序完成这个“密码薄”的增删改查功能，并且实现文件存储功能
目标 5chapter_test文件夹 pass文件
'''

import os
import Student
os.chdir("./5chapter_test") # 改变当前的路径

# 初始化
Student.initStudent()
# 增删改查 循坏打开

webSite = input("输入一个网址：")
passWord = input("输入一个密码：")
content = {"web": webSite, "pass": passWord}

f = open("pass", "w")
f.write("web:%s\npass:%s"%(content["web"], content["pass"]))
f.close()



