"""

小练习
1. 匹配网址
有一批网址：

http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
需要 正则后为：

http://www.interoem.com/
http://3995503.com/
http://lib.wzmc.edu.cn/
http://www.zy-ls.com/
http://www.fincm.com/
2. 找出单词
有一句英文如下：

hello world ha ha

查找所有的单词

"""
import re


s = """
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""

res_1 = re.findall(r"http://.+?/", s)  # 方法一
for re_i in res_1:
    print(re_i)


def replace(result):  # 方法二
    # print(result.group(1))
    return result.group(1)


res_2 = re.sub(r"(http://.+?/).*", replace, s)  # 方法二
print(res_2)


res_3 = re.sub(r"(http://.+?/).*", lambda x: x.group(1), s)  # 方法三
print(res_3)

s2 = "hello world ha ha"

# res_4 = re.findall(r"\w+?\b", s2)
# res_4 = re.split(r" +", s2)
res_4 = re.findall(r"\b[a-zA-Z]+\b", s2)
print(res_4)