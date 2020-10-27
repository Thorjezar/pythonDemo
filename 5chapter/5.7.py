# coding=utf-8

'''
import os
重命名文件 os.rename('旧文件名','新文件名')
删除文件 os.remove()

文件夹相关操作
os.mkdir("文件夹名称")   创建
os.getcwd() 获取当前目录
os.chdir("../")  改变默认目录
os.listdir("./") 获取目录列表
os.rmdir("张三") 删除文件夹
'''

# 批量在文件名前加减文字
import os
os.chdir("./test")


for temp in os.listdir():
    oldFilename = temp
    # 批量新增
    # newFilename = "[伟民制造]" + temp
    # 批量减少
    num = len("[伟民制造]")
    newFilename = temp[num:]

    os.rename(oldFilename, newFilename)


