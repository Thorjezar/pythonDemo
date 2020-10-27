# coding=utf-8

'''
同样，在操作文件的整体过程与使用word编写一份简历的过程是很相似的

打开文件，或者新建立一个文件 open()
读/写数据
关闭文件 close()
'''

f = open('text.txt', 'w')
f.write('hello world,i am here!')
f.close()
