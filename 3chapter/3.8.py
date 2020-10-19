#conding=utf-8

#列表的删除 del()下标   pop（）最末端  remove根据元素的值去修改
nameList = ["xiaoHua","xiaoYue","xiaoMin"]

findName = input("请输入要查找的姓名")

if findName in nameList:
    print("找到相同")
else:
    print("未找到")
