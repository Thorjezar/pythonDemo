# coding=utf-8

'''

打包模块使用的方法
from distutils.core import setup
setup(name="dongGe", version="1.0", description="dongGe's module", author="dongGe", py_modules=['suba.aa', 'suba.bb', 'subb.cc', 'subb.dd'])
                                                                                                  包名.模块名

构建模块
python setup.py build   python2构建
python3 setup.py build      python3构建

生成发布压缩包
python3 setup.py sdict    打包后,生成最终发布压缩包dongGe-1.0.tar.gz , 目录结构
.
├── build    构建的py包
│   └── lib.linux-i686-2.7
│       ├── suba
│       │   ├── aa.py
│       │   ├── bb.py
│       │   └── __init__.py
│       └── subb
│           ├── cc.py
│           ├── dd.py
│           └── __init__.py
├── dist    打包的py包
│   └── dongGe-1.0.tar.gz
├── MANIFEST
├── setup.py
├── suba
│   ├── aa.py
│   ├── bb.py
│   └── __init__.py
└── subb
    ├── cc.py
    ├── dd.py
    └── __init__.py
'''