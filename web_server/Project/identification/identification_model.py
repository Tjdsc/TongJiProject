#!/usr/bin/python3
from common_utils import *
from basic.basic_model import get_capacity, get_config


def calculate_all_online_degree(name, config):
    all_cycle, all_capacity = get_capacity(name, config)
    degree = []
    valid_length = []
    for cycle_end in np.arange(1, len(all_capacity)):
        capacity = all_capacity[:cycle_end]
        cycle = all_cycle[:cycle_end]
        filtered_capacity = filter_capacity(capacity)
        _, max_index = find_max(filtered_capacity)
        filtered_capacity = filtered_capacity[max_index:]
        partly_cycle = cycle[max_index:]
        valid_length.append(len(partly_cycle))
        normalized_cycle = normalization(partly_cycle)
        normalized_capacity = normalization(filtered_capacity)
        square = integral(normalized_cycle, normalized_capacity)
        score = 2 * square - 1
        degree.append(score * 100)
    return degree, valid_length


def calculate_all_online_rank(name, config):
    degree, valid_length = calculate_all_online_degree(name, config)
    rank_threshold = config['rank_threshold']
    silent_time = config['silent_time']
    rank = []
    diff_cycle = []
    r = 0
    for i in range(len(degree)):
        if valid_length[i] >= silent_time:
            if degree[i] > rank_threshold[r][0] and degree[i - 1] > rank_threshold[r][0] and degree[i - 2] > \
                    rank_threshold[r][0]:
                r += 1
                diff_cycle.append(i + 1)
            elif degree[i] < rank_threshold[r][1] and degree[i - 1] < rank_threshold[r][1] and degree[i - 2] < \
                    rank_threshold[r][1]:
                r -= 1
                diff_cycle.append(i + 1)
        else:
            if r != 0:
                diff_cycle.append(i + 1)
            r = 0
        rank.append(r)
    return rank, diff_cycle


if __name__ == '__main__':
    print(calculate_all_online_degree('b1c4', get_config(0)))
    print(calculate_all_online_rank('b1c4', get_config(0)))
