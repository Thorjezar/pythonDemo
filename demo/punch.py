#coding=utf-8
import random
import funcs

flags = 1
name = input("玩家名称:")
while flags == 1:
    player = input("请输入猜拳:剪刀(0) 石头(1) 布(2)")
    computer = random.randint(0,2)
    computer = str(computer)
    #print(computer)
    playerPunch = funcs.changePunch(player)
    computerPunch = funcs.changePunch(computer)
    result = funcs.contend(playerPunch, computerPunch)
    print("玩家%s使出了 %s ！;而电脑则使出了 %s ！,最终 %s " % (name, playerPunch, computerPunch, result))
    count = input("是否退出？[输入0.退出游戏]")
    if count == "0":
        flags = 0
'''测试
print("玩家%s,使出了%s;而电脑则使出了%s"%(name,playerPunch,computerPunch))
'''
