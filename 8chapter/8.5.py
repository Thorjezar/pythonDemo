# coding=utf-8

'''
异常

如果要捕获某个异常，那么就使用 元组 （ ） 括起来进行识别
如果捕获不到异常，那么就使用Exception来进行捕获
如果没有异常，else会执行
使用finally的话，不管是否捕获到异常都会执行

'''

try:
    # 11/0
    # open("xxx.txt")
    # print(num)
    print("-" * 8 + num + "-" * 8)
    print("-" * 8 + "1" + "-" * 8)
except (NameError, FileNotFoundError):   # 使用元组进行识别
    print("捕获到异常，并输出")
    print("捕获到文件异常")
# except Exception as ret:   # 使用as来起一个别名
#     print("如果使用了Exception，那么上面的except没有捕获到异常，那么这个except这里面就一定会捕获到")
#     print(ret)
else:
    print("如果没有异常的话会输出")
finally:
    print("不管是否捕获到异常，都要进行")

print("-" * 8 + "2" + "-" * 8)

