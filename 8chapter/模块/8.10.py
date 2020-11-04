# coding=utf-8

'''
python中的模块，是指py文件
一个py文件就是一个模块

import 模块名
使用函数时 模块名.函数名
1.3 使用import 文件.模块 的方式导入


from 模块名 import 函数名1,函数名2    导入一个模块中指定的函数
通过这种方式引入的时候，调用函数时只能给出函数名，不能给出模块名，但是当两个模块中含有相同名称函数的时候，后面一次引入会覆盖前一次引入。
也就是说假如模块A中有函数function( )，在模块B中也有函数function( )，如果引入A中的function在先、B中的function在后，
那么当调用function函数的时候，是去执行模块B中的function函数。

from 模块名 import * 一次性导入模块下的所有函数
使用from 文件夹 import 模块 的方式导入

import 模块名 as 别名
from 模块名 import 函数名1 as 别名

as 既可以用来作为模块的别名，也可以用来作为函数的别名,
调用的使用有别名则必须使用别名

'''


'''
<6>定位模块
当你导入一个模块，Python解析器对模块位置的搜索顺序是：

当前目录
如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
'''

