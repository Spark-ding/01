#导入模块:方法一
# import utils.my_fun
# utils.my_fun.log_separator1()

#方法二（需在__init__中提前配置模块）
from utils import *
my_fun.log_separator1()

#直接导入功能（函数）
from utils.my_fun import log_separator1, log_separator3

#绝对路径：从项目的根目录下开始查找
from 第六章.utils.my_fun import log_separator1, log_separator3



