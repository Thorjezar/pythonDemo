#coding=utf-8

'''
1. 编程实现对一个元素全为数字的列表，求最大值、最小值
'''

a = []

listLen = input("设定列表的长度：")
listLen = int(listLen)
print("数组的长度为%d"%listLen)

i = 0
while i < listLen:
    j = i + 1
    b = input("请输入第%d项的值"%j)
    a.append(b)
    i += 1

print("生成的数组：%s\n"%a)

print("数组的最大值为：%s\n"%max(a))

print("数字的最小值为：%s\n"%min(a))