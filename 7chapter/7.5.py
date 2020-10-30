# coding=utf-8

'''

多重继承
注意点：
如果一个子类继承多个父类
中有同名方法，子类对象在调用的时候会怎么执行
类名.__mro__ 采用C3算法，生成一个元组

'''

class Base(object):   # 加object 的是定义一个新式类，如果不加,就是经典类 python3中默认所有类都继承自object
    def fun(self):
        print("=" * 7)

class A(Base):
    # def fun1(self):
    def fun(self):
        print("A")

class B(Base):
    # def fun2(self):
    def fun(self):
        print("B")
class C(B, A):
    def fun(self):
        print("C")

c = C()
c.fun()
print(C.__mro__)   # 类名.__mro__ 查看 决定着 调用一个方法时候，搜索的顺序；如果在某个类中找到了方法，则停止搜索；采用C3算法




