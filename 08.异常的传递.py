def fun1():
    print("进入fun1")
    fun2()

def fun2():
    print("进入fun2")
    fun3()

def fun3():
    print("进入fun3")
    print(my_value)

print("成功传入GitHub")

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序错误，错误信息：", e)