#!/usr/bin/env python
# encoding: utf-8
from functools import wraps
from flask import Flask, url_for, render_template, redirect, request, jsonify, Response, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate
import DataCombinations
import DataCharts
import DataRandom
import OpenData_ydniu
import OpenData_ydniu_dlt
import OpenData_ydniu_ssq

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/lotterys.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class OpenNumber(db.Model):
    __tablename__ = 'open_numbers'
    id = db.Column(db.Integer, primary_key=True)
    data_period = db.Column(db.String(20))
    data_award = db.Column(db.String(50))
    data_type = db.Column(db.String(10))
    data_value = db.Column(db.String(10))
    data_span = db.Column(db.String(10))
    data_size = db.Column(db.String(10))
    data_qiou = db.Column(db.String(10))
    data_zhihe = db.Column(db.String(10))

    def __init__(self, data_period, data_award, data_type, data_value, data_span, data_size, data_qiou, data_zhihe):
        self.data_period = data_period
        self.data_award = data_award
        self.data_type = data_type
        self.data_value = data_value
        self.data_span = data_span
        self.data_size = data_size
        self.data_qiou = data_qiou
        self.data_zhihe = data_zhihe


class OpenNumber_Ssq(db.Model):
    __tablename__ = 'open_numbers_ssq'
    id = db.Column(db.Integer, primary_key=True)
    data_period = db.Column(db.String(20))
    data_award = db.Column(db.String(50))

    def __init__(self, data_period, data_award):
        self.data_period = data_period
        self.data_award = data_award


class OpenNumber_Dlt(db.Model):
    __tablename__ = 'open_numbers_dlt'
    id = db.Column(db.Integer, primary_key=True)
    data_period = db.Column(db.String(20))
    data_award = db.Column(db.String(50))

    def __init__(self, data_period, data_award):
        self.data_period = data_period
        self.data_award = data_award


def cors(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        r = make_response(func(*args, **kwargs))
        r.headers['Access-Control-Allow-Origin'] = '*'
        r.headers['Access-Control-Allow-Methods'] = 'HEAD, OPTIONS, GET, POST, DELETE, PUT'
        allow_headers = "Referer, Accept, Origin, User-Agent, X-Requested-With, Content-Type"
        r.headers['Access-Control-Allow-Headers'] = allow_headers
        return r

    return wrapper_func


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@app.route('/lottery/getOpenData', methods=['POST'])
@cors
def get_open_info():
    if request.method == 'POST':
        date = request.form['date']
        openNumber = OpenNumber.query.filter(
            OpenNumber.data_period.like(date + "%") if date is not None else "").all()
        numberJson = OpenData_ydniu.getOpenNumbers(openNumber)
        return return2Json(numberJson)
    return '暂无数据'


@app.route('/lottery/getOpenDataOf', methods=['POST'])
@cors
def get_open_data():
    if request.method == 'POST':
        lotteryType = request.form['type']
        if lotteryType == 'ssq':
            openNumber_ssq = OpenNumber_Ssq.query.order_by(OpenNumber_Ssq.data_period.desc()).all()
            numberJson = OpenData_ydniu_ssq.getOpenNumbers(openNumber_ssq)
            return return2Json(numberJson)
        elif lotteryType == 'dlt':
            openNumber_dlt = OpenNumber_Dlt.query.order_by(OpenNumber_Dlt.data_period.desc()).all()
            numberJson = OpenData_ydniu_dlt.getOpenNumbers(openNumber_dlt)
            return return2Json(numberJson)
    return '暂无数据'


@app.route('/lottery', methods=['POST'])
@cors
def get_numbers():
    if request.method == 'POST':
        method = request.form['type']
        numbers = request.form['numbers']
        scNumber = request.form['sc']
        ddNumber = request.form['dd']
        dxbNumber = request.form['dxb']
        qobNumber = request.form['qob']
        numberJson = DataCombinations.getForecastNumbers(method, numbers, scNumber, ddNumber, dxbNumber, qobNumber)
        return return2Json(numberJson)
    return '暂无数据'


@app.route('/lottery/jx', methods=['POST'])
@cors
def get_jx_numbers():
    if request.method == 'POST':
        method = request.form['type']
        count = request.form['count']
        numberJson = DataRandom.get_jx_numbers(method, count)
        return return2Json(numberJson)
    return '暂无数据'


@app.route('/lottery/getTypeCountDay', methods=['POST'])
@cors
def get_type_count_day():
    if request.method == 'POST':
        day = request.form['day']
        json = DataCharts.getDayTypeCounts(day)
        return return2Json(json)
    return '暂无数据'


@app.route('/lottery/getDxbCountDay', methods=['POST'])
@cors
def get_dxb_count_day():
    if request.method == 'POST':
        json = DataCharts.getDayDxbCounts()
        return return2Json(json)
    return '暂无数据'


@app.route('/lottery/getQobCountDay', methods=['POST'])
@cors
def get_qob_count_day():
    if request.method == 'POST':
        json = DataCharts.getDayQobCounts()
        return return2Json(json)
    return '暂无数据'


def return2Json(json):
    return Response(json, mimetype='application/json')


# with app.test_request_context():
#     print(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)
