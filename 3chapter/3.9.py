#coding=utf-8

#一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

import random

#定义办公室
places = [[],[],[]]

#定义老师名称
names = ["a","b","c","d","e","f","g","h"]

for name in names:
    index = random.randint(0,2)
    places[index].append(name)

i = 1

for tempName in places:
    print("办公室%d中人数有:%d"%(i,len(tempName)))
    i+=1
    for name in tempName:
        print("%s"%name,end=" ")
    print("\n")
    print("="*20)
