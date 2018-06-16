#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, url_for, render_template, redirect, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate
import DataCombinations
import OpenData

app = Flask(__name__)
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

    def __init__(self, data_period, data_award, data_type):
        self.data_period = data_period
        self.data_award = data_award
        self.data_type = data_type

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/lottery/getOpenData', methods=['POST'])
def get_open_info():
    if request.method == 'POST':
        date = request.form['date']
        openNumber = OpenNumber.query.filter(
            OpenNumber.data_period.like(date + "%") if date is not None else "").all()
        numberJson = OpenData.getOpenNumbers(openNumber)
        return return2Json(numberJson)
    return '暂无数据'

@app.route('/lottery', methods=['POST'])
def get_numbers():
    if request.method == 'POST':
        method = request.form['type']
        numbers = request.form['numbers']
        numberJson = DataCombinations.getForecastNumbers(method, numbers)
        return return2Json(numberJson)
    return '暂无数据'

def return2Json(json):
    return Response(json, mimetype='application/json')


# with app.test_request_context():
#     print(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)
