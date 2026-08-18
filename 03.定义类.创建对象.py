#定义类   ----->  不推荐动态地为对象添加属性
class Car:
    pass

#创建对象
c1 = Car()

#动态地为对象添加属性
c1.color = "black"
c1.brand = "Porsche"
c1.name = "911"
c1.price = 1000000

print(c1)
print(c1.__dict__)      #将对象中的所有属性以字典的形式输出出来