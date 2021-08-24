# !/usr/bin/python3
from scipy.signal import savgol_filter
import sys
import numpy as np
import os
import pandas as pd
import pickle
import json


def filter_capacity(capacity, window=35):
    """
    需要考虑下窗口选取的策略
    """
    window = min(window, ((len(capacity) - 1) // 2) * 2 + 1)
    order = min(window - 1, 2)
    try:
        return savgol_filter(capacity, window_length=window, polyorder=order)
    except Exception as e:
        print(e)
        return savgol_filter(capacity, window_length=window, polyorder=order)


def find_max(arr):
    """
    :param arr: 输入数组
    :return: 数组中的最大值和所在的索引
    """
    index = -1
    max_val = -sys.maxsize - 1
    for i, num in enumerate(arr):
        if num > max_val:
            index = i
            max_val = num
    return max_val, index


def normalization(data):
    """
    :param data: 原始数据
    :return: 按最大-最小值归一化之后得到的数据
    """
    _range = np.max(data) - np.min(data)
    if range != 0:
        return (data - np.min(data)) / _range
    else:
        return 0 * np.ones_like(data)


def integral(x, y):
    ans = 0.0
    for i in range(len(x) - 1):
        ans += (y[i] + y[i + 1]) * (x[i + 1] - x[i])
    return ans / 2


def concatenate_data(df1, df2):
    if len(df1) > len(df2):
        return concatenate_data(df2, df1)
    if len(df1) == 0:
        return df2
    if isinstance(df1, pd.DataFrame):
        return df1.append(df2)
    elif isinstance(df1, np.ndarray):
        return np.append(df1, df2, axis=0)
    raise Exception('未知的类型')
