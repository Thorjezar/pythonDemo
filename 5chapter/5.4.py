# coding=utf-8

'''
文件复制的程序,输入文件的名字，然后程序自动完成对文件进行备份
'''



f = open('源文件.txt', 'w+')
f.write("I'm YWM\n welcome my increatbale world\n I want to show you the fantasy world")
f.close()

f2 = open('源文件.txt', 'r+')
content = f2.readlines()
f2.close()

f3 = open('源文件(复制).txt', 'w')
for temp in content:
    f3.write(temp)

f3.close()