#coding=utf-8

'''
用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。

Lambda函数能接收任何数量的参数但只能返回一个表达式的值
匿名函数不能直接调用print，因为lambda需要一个表达式
用法1.作为函数参数传递
用法2.作为内置函数的参数传递
'''

sum = lambda arg1, arg2: arg1 + arg2

# print("3和5的和:%d"%sum(3,5)

def fun(a ,b ,opt):
    print("a=%s"%a)
    print("b=%s"%b)
    print("result=%s"%opt(a,b))

# fun(3,4,lambda x,y:x+y) 方法一

stus = [{'name': 'lisi', 'age': 18}, {'name': 'zhangsan', 'age': 24}, {'name': 'wangwu', 'age': 35}]

# stus.sort(key=lambda x: x['name']) 按照姓名排序

stus.sort(key=lambda x: x['age'])
print(stus)






