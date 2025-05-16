import itertools
import math

# 城市坐标
cities = [[0, 2], [12, 64], [16, 0], [25, 87], [32, 79], [52, 95], [57, 100], [66, 38], [68, 6], [69, 55], [92, 38], [100, 91]]
start_city = 0

# 计算两点之间的欧几里得距离
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 计算路径的总成本
def total_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += distance(path[i], path[i + 1])
    # 返回起点
    cost += distance(path[-1], start_city)
    return cost

# 生成除起点外的所有城市排列
other_cities = list(range(1, len(cities)))
permutations = itertools.permutations(other_cities)

# 初始化最小成本
min_cost = float('inf')

# 遍历所有排列
for perm in permutations:
    path = [start_city] + list(perm)
    cost = total_cost(path)
    if cost < min_cost:
        min_cost = cost

# 四舍五入到整数
min_cost = round(min_cost)

print("最短环路总成本:", min_cost)
    