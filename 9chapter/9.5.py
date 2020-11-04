# coding=utf-8

'''

range()  列表生成器

range() 在python2中的风险是 range(1,1000000000000)  值取超过 内存风险
        在python3中解决的方法时 取一个值就给开辟一个内存空间，没有取到就不会开辟额外的内存

'''

a = [i for i in range(1, 18)]
print(a)

b = [11 for i in range(10, 18)]
print(b)

c = [i for i in range(10) if i%2==0]
print(c)

d = [(i, j) for i in range(3) for j in range(2)]
print(d)

e = [(i, j, k) for i in range(3) for j in range(2) for k in range(3)]
print(e)