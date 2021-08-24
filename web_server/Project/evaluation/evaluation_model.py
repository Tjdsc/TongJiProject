#!/usr/bin/python3
from common_utils import *
from basic.basic_model import get_capacity, get_config


# 计算转折点
def calculate_knee_point(name, config):
    cycle, capacity = get_capacity(name, config)
    capacity = filter_capacity(capacity)
    _, max_index = find_max(capacity)
    # 抽出下降段
    capacity = capacity[max_index:]
    cycle = cycle[max_index:]
    normalized_cycle = normalization(cycle)
    normalized_capacity = normalization(capacity)
    distance = [(normalized_capacity[i] + normalized_cycle[i] - 1) / np.sqrt(2) for i in range(len(normalized_cycle))]
    # 找到全局最大值，作为拐点
    _, max_index = find_max(distance)
    return cycle[max_index]


# 计算转折程度
def calculate_knee_degree(name, config):
    cycle, capacity = get_capacity(name, config)
    capacity = filter_capacity(capacity)
    capacity = filter_capacity(capacity)
    _, max_index = find_max(capacity)
    # 抽出下降段
    capacity = capacity[max_index:]
    cycle = cycle[max_index:]
    normalized_cycle = normalization(cycle)
    normalized_capacity = normalization(capacity)
    distance = [(normalized_capacity[i] + normalized_cycle[i] - 1) / np.sqrt(2) for i in range(len(normalized_cycle))]
    _, max_index = find_max(distance)
    x = normalized_cycle[max_index]
    y = normalized_capacity[max_index]
    angle = np.arccos(((x ** 2 + (y - 1) ** 2) + ((x - 1) ** 2 + y ** 2) - 2) / (2 * np.sqrt(
        (x ** 2 + (y - 1) ** 2) * ((x - 1) ** 2 + y ** 2)))) / np.pi * 180
    square = integral(normalized_cycle, normalized_capacity) - 0.5
    return (180 - angle) / 90 * 100, square * 2 * 100


if __name__ == '__main__':
    print(calculate_knee_point('b1c4', get_config(0)))
    print(calculate_knee_degree('b1c4', get_config(0)))
