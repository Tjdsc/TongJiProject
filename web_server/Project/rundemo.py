from flask import Flask, jsonify, request, render_template
# from basic.basic_model import *
# from evaluation.evaluation_model import *
# from identification.identification_model import *
# from prediction.prediction_model import *
from flask_cors import *
from werkzeug.utils import secure_filename
import logging
import createAllJSON

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
# 解决跨域请求资源被拦截问题
CORS(app, supports_credentials=True, resources=r"/*")


@app.route('/')
def catch_index():
    return render_template("index.html")


@app.route('/batterymanage.html')
def catch_batterymanage():
    return render_template("batterymanage.html")


@app.route('/DataUploadView', methods=['GET', 'POST'])
def upload_file():
    global allCellDataDict
    global nameListDict
    
    store_file_path = r'upload_files/'
    file_buffer = request.files.get('file')
    file_info = dict(request.form)
    f_name = secure_filename(file_buffer.filename)
    data = {"code": 500, "msg": "上传失败！"}
    try:
        file_buffer.save(store_file_path + f_name)
        data.update({"code": 200, "msg": "上传成功！"})
    except FileNotFoundError as e:
        logging.log("error", e)
    nameListDict, allCellDataDict = createAllJSON.createAllCellData()
    return jsonify(data)


def catch_DataUploadView():
    return render_template("batterymanage.html")


@app.route('/ProcessedData', methods=['GET'])
def return_ProcessedData():
    global allCellDataDict

    if request.method == 'GET':
        try:
            response_data = allCellDataDict       
            return jsonify(response_data)        
        except Exception as e:
            return jsonify({'status': 'fail'})

@app.route('/NameList', methods=['GET'])
def return_NameList():
    global nameListDict

    if request.method == 'GET':
        try:
            response_data = nameListDict       
            return jsonify(response_data)        
        except Exception as e:
            return jsonify({'status': 'fail'})


@app.route('/DataProcessView')
def catch_DataProcessView():
    return render_template("batterymanage.html")


@app.route('/DataMonitorView')
def catch_DataMonitorView():
    return render_template("batterymanage.html")


@app.route('/casecentre.html')
def catch_casecentre():
    return render_template("casecentre.html")


@app.route('/news.html')
def catch_news():
    return render_template("news.html")


@app.route('/about.html')
def catch_about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
