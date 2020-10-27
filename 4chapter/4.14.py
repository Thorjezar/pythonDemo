#coding=utf-8

'''
阶乘的递归，递归就是自己调用自己来完成数据操作
'''

def calNum(a):
    if a > 1:
        result = a * calNum(a - 1)
        return result
    else:
        result = 1
        return result
a = int(input("请输入阶乘的因子："))

print("阶乘是：%d"%calNum(a))
