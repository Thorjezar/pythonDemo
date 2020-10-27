#coding=utf-8

'''
有时可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，声明时不会命名。

加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。
'''

def Fun1(a,b,*args,**kwargs):
    print("a=",a)
    print("b=",b)
    print("args=",args)
    for key,value in kwargs.items():
        print(key, "=", value)

Fun1(1,2,3,4,5,m = 6,n = 7,p = 8)
