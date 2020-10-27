# coding=utf-8

'''
使用read(num)可以从文件中读取数据，num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据

注意：

如果open是打开一个文件，那么可以不用写打开的模式，即只写 open('test.txt')
如果使用读了多次，那么后面读取的数据是从上次读完后的位置开始的
'''

f = open('text.txt', 'r')
# content = f.read(5)
# print(content)
# print("=" * 10)
# content = f.read()
# print(content)
# f.close()

'''
就像read没有参数时一样，readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
readline 是读一行 的字符串
读大文件的时候，禁止使用read
'''

content = f.readlines()
print(type(content))

i = 1
for temp in content:
    print("%d.%s"%(i, temp))
    i += 1

f.close()
