# coding=utf-8

'''
输入文件的名字，然后程序自动完成对文件进行备份
创建新文件，并填充内容，最后复制
'''

fileName = input("请输入文件名称：")

oldFile = open(fileName, "w+")
oldFile.write("I'm YWM\n Nice to meet U\n emmmm \n I want to talk with you \n would you like to talk me ?")
oldFile.close()

oldFile = open(fileName, 'r')

if oldFile:
    # 提取文件的后缀名
    fileFlagNum = fileName.rfind(".")
    if fileFlagNum > 0:
        fileFlag = fileName[fileFlagNum:]
        # 组织新的文件名
        newFilename = fileName[:fileFlagNum] + '(复件)' + fileFlag
    else:
        newFilename = fileName + '(复件)'

    # 创建新文件
    newFile = open(newFilename, 'w+')

    # 把旧文件的追条数据都填加进新文件
    for temp in oldFile.readlines():
        newFile.write(temp)

    # 关闭文件
    oldFile.close()
    newFile.close()