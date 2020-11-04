# coding=utf-8

'''

python的包
包将有联系的模块组织在一起，即放到同一个文件夹下，
并且在这个文件夹创建一个名字为__init__.py 文件，那么这个文件夹就称之为包
有效避免模块名称冲突问题，让应用组织结构更加清晰

__init__.py 控制着包的导入行为

__init__.py为空：仅仅是把这个包导入，不会导入包中的模块

在__init__.py文件中，定义一个__all__变量，它控制着 from 包名 import *时导入的模块
__all__ = [] 格式

Phone/
    __init__.py
    common_util.py
    Voicedta/
        __init__.py
        Pots.py
        Isdn.py
    Fax/
        __init__.py
        G3.py
    Mobile/
        __init__.py
        Analog.py
        igital.py
    Pager/
        __init__.py
        Numeric.py

import Phone.Mobile.Analog
Phone.Mobile.Analog.dial()

第一种方法是只导入顶层的子包，然后使用属性/点操作符向下引用子包树：
from Phone import Mobile
Mobile.Analog.dial('555-1212')

from Phone.Mobile import Analog
Analog.dial('555-1212')

from Phone.Mobile.Analog import dial
dial('555-1212')

同样也支持
from package.module import *
这样导入需要__init__.py中加入__all__来控制导入的模块

'''