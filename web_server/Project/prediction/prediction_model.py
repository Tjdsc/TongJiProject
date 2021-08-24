#!/usr/bin/python3

from tensorflow.keras.models import load_model
from special_utils import *
from common_utils import *
from basic.basic_model import get_capacity, get_config

applied_feature = [
    'abs_IC_DV_max',
    'abs_IC_DV_max_pos',
    'IR',
    'abs_DTV_max',
    'abs_DTV_max_pos',
    # 'Tavg_D',
    # 'Tmin_D',
    # 'Tmax_D',
    # 'Tdiff_D',
    # 'QD',
]

applied_target = [
    'CTK',
]


def my_standard_scaler(dataset, train_name_list):
    data = pd.DataFrame()
    for name in train_name_list:
        data = concatenate_data(data, dataset[name]['data'])
    train_mean = data.mean(axis=0)
    train_std = data.std(axis=0)
    return train_mean, train_std


def calculated_predicted_CTK(name, config):
    window_size = config['window_size']
    model_path = r'models/knee_point/model_{}.h5'.format(window_size)
    if not os.path.exists(model_path):
        raise Exception('窗口大小下未训练模型')
    model = load_model(model_path)
    dataset = load_dataset()
    train_name, _ = load_train_test_split()
    train_mean, train_std = my_standard_scaler(dataset, train_name)
    data, targets = get_window_info(dataset, [name], window_size, applied_feature=applied_feature,
                                    applied_target=applied_target, only_target=False)
    for parameter in data:
        data[parameter] -= train_mean[parameter]
        data[parameter] /= train_std[parameter]
    prediction = model.predict(data)
    predicted_CTK = prediction.reshape(len(targets))
    true_CTK = targets.reshape(len(targets))
    return predicted_CTK.tolist(), true_CTK.tolist()


if __name__ == '__main__':
    print(calculated_predicted_CTK('b3c8', get_config(0)))
