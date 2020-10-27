# coding=utf-8
'''
必须完成的功能：添加、删除、修改、查询、退出
'''

def initStudent():
    print("=" * 8 + "欢迎来到实力至上主义的教室"+"=" * 8)
    print(" " * 8 + "1.查看学生信息")
    print(" " * 8 + "2.新增学生信息")
    print(" " * 8 + "3.修改学生信息")
    print(" " * 8 + "4.删除学生信息")
    print(" " * 8 + "5.退出系统")
    print("=" * 41)
    j = input("请输入要操作的序号：")
    return int(j)


def addStudent(a, **b):
    return
