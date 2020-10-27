#coding=utf-8

'''
2. 编写程序，完成以下要求：
统计字符串中，各个字符的个数
比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
'''

str = input("请输入一些字符串：")

print("输入的字符串是：%s"%str)
print("||字符|| ：||个数||")

dictA = {}
for item in str:
    i = str.count(item)
    if item not in dictA.keys():
        dictA[item] = i

for key,value in dictA.items():
    print("||%s|| ：||%d||"%(key,value))

