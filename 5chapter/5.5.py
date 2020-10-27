# coding=utf-8

'''
查看文件定位的位置 f.tell()
定位文件到某处 f.seek()

seek(offset, from)有2个参数

offset:偏移量====微调 python2支持负数，3不支持

from:方向
0:表示文件开头
1:表示当前位置
2:表示文件末尾
'''

f = open("测试", "r")
content = f.read(5)
print(content)

i = f.tell()
print(i)

f.seek(5, 0)
i = f.tell()
print(i)

content = f.read(6)
print(content)


