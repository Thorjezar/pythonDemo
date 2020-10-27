# coding=utf-8

'''
读取一个文件，显示除了以井号(#)开头的行以外的所有行
目标 test1
'''

import os
os.chdir("./5chapter_test") # 将当前路径改写为目标路径

f = open("test1", "r")
# 方法一
# for temp in f.readlines():
#     if temp[0] != "#":
#         print(temp, end=" ")

# 方法二 readline()
# i = 1
# while i == 1:
#     content = f.readline()
#     if content == "":
#         i = 0
#         break
#     else:
#         if content[0] != "#":
#             print(content, end=" ")

# 方法三 seek()


f.close()