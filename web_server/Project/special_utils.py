#!/usr/bin/python3
# 特殊的工具类，针对A123数据集设计

from common_utils import *

SAMPLE_POINTS_PER_CYCLE = 1000
NONLINEAR_TYPE_NUM = 9


def load_data(only_capacity=True):
    """
    :return: 清洗后的数据
    """
    clean_batch_path = r'data\clean_bat_dict.pkl'
    only_capacity_path = r'data\clean_bat_dict_only_capacity.pkl'
    if only_capacity:
        return pickle.load(open(only_capacity_path, 'rb'))
    else:
        return pickle.load(open(clean_batch_path, 'rb'))


def load_train_test_split():
    split_path = r'data\train_test_split.json'
    split_dict = json.load((open(split_path, 'r')))
    return split_dict['train'], split_dict['test']


def load_dataset():
    dataset_path = r'data\dataset.pkl'
    return pickle.load(open(dataset_path, 'rb'))


def get_window_info(dataset, name_list, window_size, applied_feature=[], applied_cnn_feature=[],
                    applied_target=[], only_target=True):
    """
    :param dataset: 循环特征数据集
    :param name_list: 电池列表
    :param applied_feature: 选取的特征
    :param applied_cnn_feature: 选取的CNN特征
    :param applied_target: 选取的输出目标
    :param window_size: 窗口大小
    :param verbose: 是否输出时间，默认False
    :param only_target: 只选取输出，默认False
    :return: 按窗口取循环特征，每一个循环下只取一维特征的集合
    """
    data = {}
    targets = []
    for name in name_list:
        cycle_num = len(dataset[name]['targets']['QD'])
        if window_size > cycle_num:
            print(
                'window_size>cycle_num, name={}, window_size={}, cycle_num={}'.format(name, window_size, cycle_num))
            continue
        targets.extend((dataset[name]['targets'][applied_target])[window_size - 1:cycle_num].values)
    count = len(targets)
    if 'CL' not in applied_target:
        targets = np.array(targets).astype(np.float32).flatten()
    else:
        targets_np = np.array([None] * count * NONLINEAR_TYPE_NUM, dtype=np.object).astype(
            np.float32).reshape((count, NONLINEAR_TYPE_NUM))
        for i in np.arange(count):
            targets_np[i] = targets[i][0]
        targets = targets_np
    if only_target:
        return targets
    for parameter in applied_feature:
        data[parameter] = np.array([None] * count * window_size, dtype=np.object).astype(np.float32).reshape(
            (count, window_size, 1))
    for parameter in applied_cnn_feature:
        data[parameter] = np.array([None] * count * window_size * SAMPLE_POINTS_PER_CYCLE, dtype=np.object).astype(
            np.float32).reshape((count, window_size, SAMPLE_POINTS_PER_CYCLE, 1))
    index = 0
    for name in name_list:
        cycle_num = len(dataset[name]['targets']['QD'])
        if cycle_num < window_size:
            continue
        # 构建初始窗口
        for parameter in applied_feature:
            data[parameter][index] = dataset[name]['data'][parameter].iloc[0:window_size].values.reshape(
                (window_size, 1))
        for parameter in applied_cnn_feature:
            for i in range(window_size):
                data[parameter][i] = dataset[name]['details'][parameter].iloc[i]
        index += 1
        # 开始滑动窗口
        for i in range(window_size, cycle_num):
            # 丢掉第一行，加上最后一行
            for parameter in applied_feature:
                data[parameter][index] = dataset[name]['data'][parameter].iloc[
                                         i + 1 - window_size:i + 1].values.reshape(
                    (window_size, 1))
            for parameter in applied_cnn_feature:
                for j in range(window_size):
                    data[parameter][j] = dataset[name]['details'][parameter].iloc[
                        i + 1 - window_size + j]
            index += 1
    return data, targets


def my_standard_scaler(dataset, train_name_list):
    data = pd.DataFrame()
    for name in train_name_list:
        data = concatenate_data(data, dataset[name]['data'])
    train_mean = data.mean(axis=0)
    train_std = data.std(axis=0)
    return train_mean, train_std
