#coding=utf-8

'''
1. 编程实现 9*9乘法表
'''

def fun1():
    i = 1
    while i <= 9:
            j = 1
            while j <= i:
                result = j * i
                print("%d * %d = %d" % (j, i, result), end="\t")
                j += 1
            print("\n")
            i += 1
fun1()
