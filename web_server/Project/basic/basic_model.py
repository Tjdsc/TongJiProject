#!/usr/bin/python3
from special_utils import *
from common_utils import *


def get_test_name():
    _, test_name = load_train_test_split()
    return test_name


def get_config(project_id=0):
    return {'soh_min': 0.8,
            'soh_max': 1,
            'nominal_capacity': 1.1,
            'rank_threshold': [
                [20, -sys.maxsize - 1],
                [35, 15],
                [50, 30],
                [sys.maxsize, 45]
            ],
            'silent_time': 30,
            'window_size': 20}


def get_capacity(name, config):
    bat_dict = load_data(only_capacity=True)
    capacity = bat_dict[name]['summary']['QD']
    soh_min = config['soh_min']
    soh_max = config['soh_max']
    nominal_capacity = config['nominal_capacity']
    cycle = np.arange(len(capacity)) + 1
    min_capacity = soh_min * nominal_capacity
    max_capacity = soh_max * nominal_capacity
    min_index = -1
    max_index = len(capacity)
    for i in np.arange(len(capacity)):
        if min_index == -1 and capacity[i] < max_capacity:
            min_index = i
        if max_index == len(capacity) and capacity[i] < min_capacity:
            max_index = i - 1
        if max_index != len(capacity) and min_index != -1:
            break
    assert max_index >= min_index
    return cycle[min_index:max_index].tolist(), capacity[min_index:max_index].tolist()


if __name__ == '__main__':
    print(get_capacity('b1c4', get_config(0)))
