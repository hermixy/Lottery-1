#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, url_for, render_template, redirect, request, jsonify
import DataCombinations

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/lottery', methods=['POST'])
def get_numbers():
    if request.method == 'POST':
        method = request.form['type']
        numbers = request.form['numbers']
        DataCombinations.initNumbers(numbers)
        if method == str("m0"):
            m0 = DataCombinations.getM0()
            return return2Json(m0)
        if method == str("m1"):
            m1 = DataCombinations.getM1()
            return return2Json(m1)
        if method == str("m2"):
            m2 = DataCombinations.getM2()
            return return2Json(m2)
        if method == str("m3"):
            m3 = DataCombinations.getM3()
            return return2Json(m3)
        if method == str("m4"):
            m4 = DataCombinations.getM4()
            return return2Json(m4)
    return '暂无数据'


def return2Json(result):
    return jsonify({"data": str(result)})


# with app.test_request_context():
#     print(url_for('hello_world'))

if __name__ == '__main__':
    app.run()
