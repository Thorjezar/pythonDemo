# coding=utf-8

'''
1.用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
'''


year = int(input("请输入年份："))
month = int(input("请输入月份："))
days = int(input("请输入日期："))

#非闰年的情况下，每个月的累计天数
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

def fun4(year, month, day):
    if 0 < month <= 12:
        sum_days = months[month - 1]  # 根据输入的月份的索引值来判断第几个月
    sum_days += days
    if year % 400 == 0:
        print("输入的年份%d为闰年" % year)
        if month > 2:
            sum_days += 1
    print("输入的日期是该年的第%d天" % sum_days)

fun4(year, month, days)







