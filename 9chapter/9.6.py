# coding=utf-8

'''

生成一个[[1,2,3],[4,5,6]....]的列表最大值在100以内

请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]

'''
a = [[i, i+1, i+2] for i in range(1, 100, 3)]
print(a)


longinput = input("请输入列表的长度：")
longinput = int(longinput)
b = [i for i in range(1, longinput)]
print("生成的原始列表是：")
print(b)
c = [[x, x+1, x+2] for x in range(1, len(b), 3)]
print("新生成的列表是：")
print(c)

