class Car:
    #初始化方法，对象创建后自动调用，主要用于设置对象的初始状态（设置对象属性）
    def __init__(self, c_brand, c_name, c_price):
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
    #示例方法
    def running(self):
        print(f"{self.brand} {self.name}正在行驶~")
    def  total_price(self, discount, rate):
        """
        计算购买汽车的总费用
        :param discount: 折扣
        :param rate: 税率
        :return: 总费用
        """
        total_cost = discount * self.price + rate * self.price
        return total_cost

    #魔法方法
    def __str__(self):                      #定义字符串本身
        return f"品牌：{self.brand} \n型号：{self.name} \n价格：{self.price}"
    def __eq__(self, other):        #定义“相等”
        return (self.price == other.price
                and self.brand == other.brand and self.name == other.name)
    def __lt__(self, other):
        return (self.price < other.price)

c1 = Car("porsche","911",1000000)

print(c1)
print(c1.__dict__)

c1.running()
total = c1.total_price(0.8, 0.1)
print(f"购车的总费用为{total}")

c2 = Car("porsche","911",800000)
print(c1 == c2)

print(c2 < c1)
print(c1 > c2)