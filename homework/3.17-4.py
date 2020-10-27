#coding=utf-8

'''
4. 编写程序，完成“名片管理器”项目
需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
程序运行后，除非选择退出系统，否则重复执行功能
'''

#初始化一个名片存储
cards = {}

i = 0
while i == 0:
    print("=" * 10 + "欢迎使用名片管理器" + "=" * 10)
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.退出系统")
    j = input("请选择使用功能系统的编号")
    j = int(j)

    #退出系统
    if j == 5:
        break
    #新增名片
    if j == 1:
        addContinue = "1"
        while addContinue == "1":
            print("=" * 20)
            info = {"name": {}, "phonenumber": {}, "wechat": {}}
            if 1 not in cards.keys():
                idKey = 1    #编号
                info["name"] = input("添加第%d个名片的姓名"%idKey)
                info["phonenumber"] = input("添加第%d个名片的电话号"%idKey)
                info["wechat"] = input("添加第%d个名片的微信号"%idKey)
                cards[idKey] = info     #添加进名片中
                print("新增名片编号%d：姓名：%s||电话号：%s||微信号：%s"%(idKey,info["name"],info["phonenumber"],info["wechat"]))
                addContinue = input("是否继续添加名片[1.填加/0.返回主菜单]")
                if addContinue == "0":
                    break

            else:
                idKey += 1
                info["name"] = input("添加第%d个名片的姓名" % idKey)
                info["phonenumber"] = input("添加第%d个名片的电话号" % idKey)
                info["wechat"] = input("添加第%d个名片的微信号" % idKey)
                cards[idKey] = info  # 添加进名片中
                print("新增名片编号%d：姓名：%s||电话号：%s||微信号：%s" %(idKey, info["name"], info["phonenumber"], info["wechat"]))
                addContinue = input("是否继续添加名片[1.填加/0.返回主菜单]")
                if addContinue == "0":
                    break
        continue
    #删除名片,先实现最基本的功能，是否存在和删除哪一项。小逻辑bug是编号1的名片不可以删除
    if j == 2:
        delContinue = "1"
        while delContinue == "1":
            print("=" * 20)
            if 1 not in cards.keys():
                print("没有名片可以删除！请返回添加名片")
                break

            else:
                print("名片库中有以下名片：")
                for id,item in cards.items():
                    print("名片编号%d：姓名：%s||电话号：%s||微信号：%s" %(id, item["name"], item["phonenumber"], item["wechat"]))

                delId = input("请输入要删除的编号：")
                delId = int(delId)

                del(cards[delId])    #删除名片
                idKey -= 1
                delContinue = input("是否继续删除？[1.继续删除/0.返回主菜单]")
                if delContinue == "0":
                    break
        continue
    #修改名片
    if j == 3:
        updateContinue = "1"
        while updateContinue == "1":
            print("=" * 20)
            info = {"name": {}, "phonenumber": {}, "wechat": {}}
            if 1 not in cards.keys():
                print("没有名片可以修改！请返回添加名片")
                break
            else:
                print("名片库中有以下名片：")
                for id,item in cards.items():
                    print("名片编号%d：姓名：%s||电话号：%s||微信号：%s" %(id, item["name"], item["phonenumber"], item["wechat"]))

                updateId = input("请输入要修改的编号：")
                updateId = int(updateId)

                info["name"] = input("修改编号%d名片的姓名" % updateId)
                info["phonenumber"] = input("修改编号%d名片的电话号" % updateId)
                info["wechat"] = input("修改编号%d名片的微信号" % updateId)
                cards[updateId] = info
                updateContinue = input("是否继续修改？[1.继续修改/0.返回主菜单]")
                if updateContinue == "0":
                    break
        continue

    #查询名片
    if j == 4:
        if 1 not in cards.keys():
            print("没有名片可以修改！请返回添加名片")
        else:
            print("名片库中有以下名片：")
            for id, item in cards.items():
                print("名片编号%d：姓名：%s||电话号：%s||微信号：%s" % (id, item["name"], item["phonenumber"], item["wechat"]))

        continue

print("系统已关闭！")
