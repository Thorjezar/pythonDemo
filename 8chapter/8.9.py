# coding=utf-8

'''
异常处理中抛出异常


'''
class Demo(object):
    def __init__(self, switch):
        self.switch = switch

    def result(self, a, b):
        try:
            return a/b
        except Exception as ret:
            if self.switch == True:
                print("捕获到异常")
                print(ret)
            else:
                # 重新抛出这个异常，从而将未捕获的异常重新抛出
                raise

a = Demo(True)
a.result(11, 0)  # 这里会打印出捕获异常

print("-" * 8 + "分割线" + "-" * 8)

a.switch = False
a.result(11, 0)  # 这里会原样输出异常

