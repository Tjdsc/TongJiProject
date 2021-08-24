from flask import Flask, jsonify, request
from basic.basic_model import *
from evaluation.evaluation_model import *
from identification.identification_model import *
from prediction.prediction_model import *
from flask_cors import *

app = Flask(__name__)
# 解决跨域请求资源被拦截问题
CORS(app, supports_credentials=True, resources=r"/*")


@app.route('/')
def hello_world():
    """
    测试是否连接上
    :return:
    """
    return 'Hello World!'


@app.route("/name_list", methods=['GET'])
def name_list():
    """
    返回所有的测试电池名称
    :return:
    """
    data = {'name': get_test_name()}
    return jsonify(data)


@app.route("/capacity", methods=['POST'])
def cell_capacity():
    """
    返回指定电池和配置下的容量数据
    :return:
    """
    name = request.form.get('name')
    project_id = int(request.form.get('project_id'))
    cycle, capacity = get_capacity(name, get_config(project_id))
    data = {'cycle': cycle, 'capacity': capacity}
    return jsonify(data)


@app.route("/knee_point", methods=['POST'])
def knee_point():
    """
    返回指定电池和配置下的转折点
    :return:
    """
    name = request.form.get('name')
    project_id = int(request.form.get('project_id'))
    knee_point = calculate_knee_point(name, get_config(project_id))
    data = {'knee_point': knee_point}
    return jsonify(data)


@app.route("/knee_degree", methods=['POST'])
def knee_degree():
    """
    返回指定电池和配置下的转折程度
    :return:
    """
    name = request.form.get('name')
    project_id = int(request.form.get('project_id'))
    angle_method, square_method = calculate_knee_degree(name, get_config(project_id))
    data = {'angle_method': angle_method, 'square_method': square_method}
    return jsonify(data)


@app.route("/online_degree_all", methods=['POST'])
def online_degree_all():
    """
    返回指定电池和配置下的实时转折程度数据（截至当前循环的所有历史数据）
    :return:
    """
    name = request.form.get('name')
    project_id = int(request.form.get('project_id'))
    online_degree, valid_length = calculate_all_online_degree(name, get_config(project_id))
    data = {'online_degree': online_degree, 'valid_length': valid_length}
    return jsonify(data)


@app.route("/online_rank_all", methods=['POST'])
def online_rank_all():
    """
    返回指定电池和配置下的等级变化曲线（截至当前循环的所有历史数据）
    :return:
    """
    name = request.form.get('name')
    project_id = int(request.form.get('project_id'))
    online_rank, diff_cycle = calculate_all_online_rank(name, get_config(project_id))
    data = {'online_rank': online_rank, 'diff_cycle': diff_cycle}
    return jsonify(data)


@app.route("/predicted_ctk", methods=['POST'])
def predicted_ctk():
    """
    返回指定电池和配置下的CTK预测结果及真值（截至当前循环的所有历史数据，扣除窗口大小）
    :return:
    """
    name = request.form.get('name')
    project_id = int(request.form.get('project_id'))
    predicted_CTK, true_CTK = calculated_predicted_CTK(name, get_config(project_id))
    data = {'predicted_ctk': predicted_CTK, 'true_ctk': true_CTK}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
