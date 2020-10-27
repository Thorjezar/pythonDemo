#coding=utf-8

'''
写一个函数求三个数的和
写一个函数求三个数的平均值
'''

def addCount(a,b,c):
    print("三个数%s %s %s的和是：%s"%(a,b,c,a+b+c))
    return a+b+c

def avgCount(a,b,c):
    print("平均值是:%d"%(addCount(a,b,c)/3.0))

sum = input("请输入三个数，以空格隔开")
a = int(sum.split(" ")[0])
b = int(sum.split(" ")[1])
c = int(sum.split(" ")[2])

avgCount(a,b,c)
