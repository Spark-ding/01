# TODO 1: 导入 random 模块 和 time 模块
import random
import time

def generate_random_graph(nodes_count, probability):
    """
    生成随机无向图的邻接表
    :param nodes_count: 节点总数
    :param probability: 两个节点之间连线的概率 (0.0 到 1.0)
    :return: 图的字典
    """
    # 初始化一个空的邻接表 (使用字典推导式，极其地道！)
    graph = {i: [] for i in range(nodes_count)}

    # TODO 2: 编写双重循环，遍历所有的节点对 (i, j)。
    # 🚨 数学逻辑避坑：因为是无向图，A连B等同于B连A，且自己不能连自己。
    # 所以外层循环 i 从 0 到 nodes_count-1，内层循环 j 应该从 i+1 到 nodes_count-1
    for i in  range (nodes_count):
        for j in range(i+1, nodes_count):

        # TODO 3: 调用 random.random()，它会生成一个 0.0 到 1.0 之间的随机浮点数。
        # 如果这个随机数 < probability，说明这两点之间有缘分，建立双向连接！
        # (即把 j 加进 graph[i] 的列表，把 i 加进 graph[j] 的列表)
            k = random.random()     #用来生成 0.0 到 1.0 之间的小数
            if k < probability:
                graph[i].append(j)
                graph[j].append(i)
    return graph


# 专业的防御机关
if __name__ == "__main__":
    print("=== 开始生成大规模随机图 ===")

    # TODO 4: 记录程序开始执行的时间戳。提示：使用 time.time()
    start_time = time.time()

    # 挑战：生成一个 1000 个节点，节点间连线概率为 5% (0.05) 的大图
    my_big_graph = generate_random_graph(1000, 0.05)

    # TODO 5: 记录结束时间戳，并计算出总耗时(秒)
    end_time = time.time()
    time_cost = end_time - start_time

    print(f"✅ 图生成完毕！总共耗时: {time_cost} 秒")

    # 抽查一下节点 0 的情况
    print(f"节点 0 的实际度数(连接的好友数): {len(my_big_graph[0])}")