from basic.basic_model import *
from evaluation.evaluation_model import *
from identification.identification_model import *
from prediction.prediction_model import *
import json




class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def createAllCellData():
    # 0.读取用户发来的干净文件(只有name,cycle,capacity的json文件)
    with open('upload_files/testJSON.json') as openRawData:
        rawData = json.load(openRawData)
        # print(rawData)

    # 1.生成NameList
    nameList = list(rawData.keys())
    nameDict = {'name':nameList}
    # count = 0
    # for name in nameList:
    #     nameDict[count] = name
    #     count += 1
    # print(nameDict)

    # 2.生成处理后的all_cell_data字典
    allcelldatadict = {"dependencies":{"all":{"0":{}}}}
    for name in nameList:
        cycle, capacity = get_capacity(name, get_config())
        knee_point = calculate_knee_point(name, get_config())
        angle_method, square_method = calculate_knee_degree(name, get_config())
        angle_degree, square_degree, valid_length = calculate_all_online_degree(name, get_config())
        online_rank, diff_cycle = calculate_all_online_rank(name, get_config())
        predicted_CTK, true_CTK = calculated_predicted_CTK(name, get_config())
        allcelldatadict['dependencies']['all']['0'][name] = {
            'capacity': {'capacity': capacity, 'cycle': cycle},
            'knee_point': {'knee_point': knee_point},
            'knee_degree': {'angle_method': angle_method, 'square_method': square_method},
            'online_degree_all': {'angle_degree': angle_degree, 'square_degree': square_degree,
                                  'valid_length': valid_length},
            'online_rank_all': {'online_rank': online_rank, 'diff_cycle': diff_cycle},
            'predicted_ctk': {'predicted_ctk': predicted_CTK, 'true_ctk': true_CTK},
        }
        # print(type(angle_degree))
        # print(angle_degree)
    # 3.全部转为list
    # for key in allcelldatadict['dependencies']['all']['0'].keys():
    #     print(type(allcelldatadict['dependencies']['all']['0'][key]))
    # #     if type(allcelldatadict.values) is  


    # 4.字典转JSON并保存
    filename = 'process_data/all_cell_data.json'
    with open(filename, 'w') as f:
        json.dump(allcelldatadict, f, cls=NpEncoder, separators=(',',':'), indent=2, allow_nan=True)
    filename = 'process_data/nameList.json'
    with open(filename, 'w') as f:
        json.dump(nameDict, f, cls=NpEncoder, separators=(',',':'), indent=2, allow_nan=True)
    # filename = 'process_data/parameter.json'
    # with open(filename, 'w') as f:
    #     json.dump(parameterDict, f, cls=NpEncoder, separators=(',',':'), indent=2, allow_nan=True)
    return nameDict, allcelldatadict
    


if __name__ == '__main__':
    createAllCellData()
