#猜拳转换函数
def changePunch( num ):
    punchDict = {"0": "剪刀", "1": "石头", "2": "布"}
    if num == "0":
        name = punchDict["0"]
    elif num == "1":
        name = punchDict["1"]
    else:
        name = punchDict["2"]
    return name
#猜拳判断函数
def contend( pun1,pun2 ):
    if ((pun1 == "剪刀" and pun2 == "布") or (pun1 == "石头" and pun2 == "剪刀") or (pun1 == "布" and pun2 == "石头")):
        result = "玩家胜利"
    elif ((pun1 == pun2)):
        result = "玩家与电脑平手"
    else:
        result = "玩家输了"
    return result

