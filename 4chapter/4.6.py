#coding=utf-8

def plusNumber(num):
    result = 1
    i = 1
    while i <= num :
        result *= i
        i += 1

    return result


num = input("输入最大的乘数")
num = int(num)
result = plusNumber(num)

print("从1至%d的累计乘为：%s"%(num,result))
