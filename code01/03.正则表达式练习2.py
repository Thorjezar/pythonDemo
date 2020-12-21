"""
提取链接中的url
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"
src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">

"""
import re


"""
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" 
src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
"""
s = """
<img class="normal" width="278px" data-loadfunc="0" 
src="https://tukuimg.bdstatic.com/scrop/4a8f2006d68d88ed2498c02a373e3b95.gif" data-loaded="0">
"""


result = re.search(r"https.+\.(jpg|gif|png)", s)  # 为什么没有加? 也关闭了贪婪模式
print(result.group())
# result = re.findall(r"https.+\.jpg", s)
# print(result)