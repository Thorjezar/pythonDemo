# coding = utf-8

'''
2. 编写“学生管理系统”，要求如下：
必须使用自定义函数，完成对程序的模块化
学生信息至少包含：姓名、年龄、学号，除此以外可以适当添加
必须完成的功能：添加、删除、修改、查询、退出
'''

import Student

# 定义一个循环标志
i = 0
# 学生信息存放初始化
ssr = {}

while i == 0:
    j = Student.initStudent()

    # 退出系统
    if j == 5:
        print("退出系统")
        i = 1
        break


