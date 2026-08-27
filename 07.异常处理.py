#异常的捕获：如果异常没有被捕获，程序会立即终止，并显示错误信息。
try:
    print("=======================")
    # print(my_name)
    # print(1 / 0)
    # print("ABC"[10])
    print("ABC".hello)
    print("========================")
except NameError as e:
    print("名字不存在，请检查变量或函数名字，异常信息：", e)
except ZeroDivisionError as e:
    print("0不能作为被除数，异常信息：",e)
except IndexError as e:
    print("索引错误，异常信息：",e)
except Exception as e:  #捕获所有异常
    print("程序运行出错了，错误信息：",e)
finally:
    print("资源释放~")