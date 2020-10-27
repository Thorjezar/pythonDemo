# coding=utf-8

'''
3.请用函数实现一个判断用户输入的年份是否是闰年的程序
'''

def fun3(year):
    if year%400 == 0:
        print("输入的%d是闰年"%year)
    else:
        print("输入的不是闰年")

a = int(input("请输入一个年份"))

fun3(a)
