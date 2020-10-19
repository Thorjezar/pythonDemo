#coding=utf-8
'''
从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
'''

account = "ywm111"
password = "123456"

a1 = input("请输入用户名")
p1 = input("请输入密码")

if a1 == account and p1 == password:
    print("欢迎进入xxx的世界")
elif a1 != account:
    print("用户名错误")
elif p1 != password:
    print("密码错误")
else:
    print("都错了 滚")