# coding=utf-8

'''
2.用函数实现求100-200里面所有的素数
'''

def fun2():
    i = 100
    while i <= 200:
        j = 2
        while j <= i:
            if i % j == 0:
                break
            else:
                j += 1
                if j == i:
                    print("100到200的素数有:%d"%i)
        i += 1

fun2()