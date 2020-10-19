#coding=utf-8

'''
字典中的每个元素的数据，都可以修改。只要能通过key值找到，即可修改
字典中的 del()删除，删除之后不能正常访问   clear（）清空整个字典

'''

ssr = {'name':'你猜','age':22,'sex':'男','address':'China'}

# print("修改前的名称是：%s"%ssr['name'])

newName = input("请输入新编号")

ssr['id'] = newName

# print("修改后的名称是：%s"%ssr['name'])

print(ssr)