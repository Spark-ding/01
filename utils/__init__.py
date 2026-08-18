#描述包信息
__version__ = "1.0.0"
__author__ = "峰哥"
__all__ = ['my_fun','my_var']
#在通过'from 包名 import *'导入全部模块的时候，
#需要在__init__.py中添加'__all__ = []'，控制允许导入的模块列表