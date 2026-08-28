import math

class Vector:
    """N维高维向量数学模型"""

    # ==========================================
    # 1. 类属性 (Class Attribute)
    # ==========================================
    # 记录整个系统一共实例化了多少个向量对象
    total_vectors = 0

    def __init__(self, *args):
        # ==========================================
        # 2. 实例属性 (Instance Attribute)
        # ==========================================
        # TODO 1: 利用 *args 的打包特性，将传入的坐标保存为元组 self.coords
        # (因为向量坐标在数学运算中绝不应该被随意篡改，用元组最安全！)
        self.coords = args

        # 每次成功实例化一个对象，全局的类属性 +1
        Vector.total_vectors += 1

    # ==========================================
    # 3. 魔法方法：格式化输出 (__str__)
    # ==========================================
    def __str__(self):
        """当 print(对象) 时触发。期望输出格式：Vector(1, 2, 3)"""
        # TODO 2: 组装并返回指定的字符串格式 (直接利用元组的打印特性即可)
        return f"Vector{self.coords}"

    # ==========================================
    # 4. 魔法方法：运算符重载 (__add__)
    # ==========================================
    def __add__(self, other):
        """
        当你执行 VectorA + VectorB 时自动触发。
        数学逻辑：将两个向量对应维度的坐标相加。
        """
        # 严谨的维度校验
        if len(self.coords) != len(other.coords):
            raise ValueError("数学错误：维度不同的向量不能相加！")

        # TODO 3: 实现向量相加。
        # 提示：利用 zip(self.coords, other.coords) 将对应坐标配对，
        # 配合列表推导式算出相加后的列表，最后将其作为参数实例化一个【全新】的 Vector 对象并返回。
        # (注意这里的解包：return Vector(*新列表))
        zipped_coords = zip(self.coords, other.coords)
        added = [i+j for i, j in zipped_coords]
        return Vector(*added)

    # ==========================================
    # 5. 实例方法 (Instance Method)
    # ==========================================
    def euclidean_distance(self, other):
        """计算当前向量与另一个向量的空间欧几里得距离"""
        if len(self.coords) != len(other.coords):
            raise ValueError("数学错误：维度不同的向量无法计算距离！")

        # TODO 4: 根据欧氏距离公式完成计算。
        # 提示：依然可以使用 zip 配对，算出差值的平方和，最后使用 math.sqrt() 开根号。
        total_dist = math.sqrt(sum((i - j) ** 2 for i, j
                                   in zip(self.coords, other.coords)))
        return total_dist
    # ==========================================
    # 6. 【拓展】类方法 (Class Method)
    # ==========================================
    @classmethod
    def get_system_stats(cls):
        """这是一个类方法，不需要实例化就能调用，专门用来查询全局状态"""
        # cls 就代表 Vector 这个类本身
        return f"系统当前共构建了 {cls.total_vectors} 个向量张量。"


# ==========================================
# 工业级数学测试区 (补全上方代码后，直接运行这里)
# ==========================================
if __name__ == "__main__":
    print("=== 数据科学向量空间引擎启动 ===\n")

    # 测试 1: 实例化与魔法方法 __str__
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(1, 1, 1, 1)  # 这是一个 4 维向量

    print(f"向量 v1: {v1}")  # 这里自动触发 __str__
    print(f"向量 v2: {v2}")

    # 测试 2: 魔法方法 __add__ 带来的极致丝滑体验
    try:
        # 这里自动触发 __add__
        v_sum = v1 + v2
        print(f"\n向量相加测试 (v1 + v2): {v_sum}")  # 期望输出: Vector(5, 7, 9)
    except Exception as e:
        print(f"相加失败: {e}")

    # 测试 3: 容错机制拦截测试
    try:
        v_error = v1 + v3
    except ValueError as e:
        print(f"维度校验成功拦截: {e}")

    # 测试 4: 实例方法 (计算欧氏距离)
    # 点(0,0) 和 点(3,4) 的直线距离，经典的勾股定理，结果必须是 5.0
    origin = Vector(0, 0)
    point = Vector(3, 4)
    dist = origin.euclidean_distance(point)
    print(f"\n原点与 (3,4) 的空间距离: {dist}")  # 期望输出: 5.0

    # 测试 5: 类方法验证 (不需要通过具体向量，直接找类要数据)
    print(f"\n{Vector.get_system_stats()}")  # 期望输出: 系统当前共构建了 6 个向量张量。