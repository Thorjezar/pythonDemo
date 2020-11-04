# coding=utf-8

'''

自定义模块
名称.pyc 是字节码文件

__name__ 属性 模块自己调用显示"__main__" 导入被调用显示模块名

可以根据__name__变量的结果能够判断出，是直接执行的python脚本还是被引入执行的，从而能够有选择性的执行测试代码



'''

def fun1(a, b):
    return a + b

def printStar():
    print("*" * 8)

print(__name__)

def main():
    pass

if __name__ == "__main__":
    # fun1(1, 2)
    # printStar()
    main()

