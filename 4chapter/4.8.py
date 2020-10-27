#coding=utf-8

'''
写一个函数打印一条横线
打印自定义行数的横线
'''

def printLine():
    print("-" * 20)

def countLine(num):
    i = 0
    while i < num :
        printLine()
        i += 1

num = input("打印几条线？")
num = int(num)

countLine(num)
