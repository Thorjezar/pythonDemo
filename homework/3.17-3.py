#coding=utf-8

'''
3. 编写程序，完成以下要求：
完成一个路径的组装
先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share
'''

counts = input("路径需要分几次进行输入？？")
counts = int(counts)

i = 0
while i < counts:
    j = i + 1
    addrs = input("输入第%d次路径："%j)
    # sumAddrs += "/" + addrs
    if i == 0:
        sumAddrs = "/" + addrs
    # elif i == counts - 1:
    #     sumAddrs += addrs
    else:
        sumAddrs += "/" + addrs

    i += 1

print("完整的路径名是：%s"%sumAddrs)
