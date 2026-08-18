
#函数
def log_separator1():
    print("-" * 30)

def log_separator2():
    print("*" * 30)


def log_separator3():
    print("#" * 30)

#测试函数
#__name__:Python中内置变量，表示当前模块的名字
# 执行当前文件，则会执行如下代码；如果被当做模块导入，如下代码不执行
#简化写法：直接输入： “main”
if __name__ == '__main__':
    log_separator1()