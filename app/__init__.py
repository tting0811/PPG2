# -*- coding: UTF-8 -*-
import app.model as model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    input = np.array([5.5])
    result =model.predict(input)
    return jsonify({'result':str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳來的數值
    insertValues = request.get_json()
    x=insertValues['x']
    input = np.array([[x]])
    # 預測
    result = model.predict(input)

    return jsonify({'return': str(result)})

'''
@app.route('/')
def index():
    return 'Flask API started!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
'''