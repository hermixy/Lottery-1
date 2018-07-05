# -*- coding: UTF-8 -*-

import Lottery
import json
import datetime
from sqlalchemy import func, case


# 近5日
def getDayTypesCount():
    # sql = "SELECT " \
    #       "count(CASE data_type WHEN 'M0' THEN 'M0' END) AS M0数量," \
    #       "count(CASE data_type WHEN 'M1' THEN 'M1' END) AS M1数量, " \
    #       "count(CASE data_type WHEN 'M2' THEN 'M2' END) AS M2数量, " \
    #       "count(CASE data_type WHEN 'M3' THEN 'M3' END) AS M3数量, " \
    #       "count(CASE data_type WHEN 'M4' THEN 'M4' END) AS M4数量  " \
    #       "FROM open_numbers WHERE data_period LIKE '180616%'"
    # openNumbers = Lottery.db.session.execute(sql).fetchall()
    # print(openNumbers)
    list = []
    for i in range(10):
        dateItem = getDate(i + 1)[2:]
        itemDict = dict()
        openNumbers = Lottery.db.session.query(
            func.count(
                case([
                    (Lottery.OpenNumber.data_type == 'M0', 'M0')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_type == 'M1', 'M1')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_type == 'M2', 'M2')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_type == 'M3', 'M3')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_type == 'M4', 'M4')
                ])),
        ).filter(Lottery.OpenNumber.data_period.like("%" + dateItem + "%") if dateItem is not None else "").all()
        # print(openNumbers)
        itemDict['date'] = dateItem
        itemDict['m0'] = openNumbers[0][0]
        itemDict['m1'] = openNumbers[0][1]
        itemDict['m2'] = openNumbers[0][2]
        itemDict['m3'] = openNumbers[0][3]
        itemDict['m4'] = openNumbers[0][4]
        list.append(itemDict)
    return list


def getDayDxbCount():
    list = []
    for i in range(5):
        dateItem = getDate(i + 1)[2:]
        itemDict = dict()
        openNumbers = Lottery.db.session.query(
            func.count(
                case([
                    (Lottery.OpenNumber.data_size == '0:5', '0:5')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_size == '1:4', '1:4')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_size == '2:3', '2:3')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_size == '3:2', '3:2')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_size == '4:1', '4:1')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_size == '5:0', '5:0')
                ])),
        ).filter(Lottery.OpenNumber.data_period.like("%" + dateItem + "%") if dateItem is not None else "").all()
        itemDict['date'] = dateItem
        itemDict['0:5'] = openNumbers[0][0]
        itemDict['1:4'] = openNumbers[0][1]
        itemDict['2:3'] = openNumbers[0][2]
        itemDict['3:2'] = openNumbers[0][3]
        itemDict['4:1'] = openNumbers[0][4]
        itemDict['5:0'] = openNumbers[0][5]
        list.append(itemDict)
    return list


def getDayQobCount():
    list = []
    for i in range(5):
        dateItem = getDate(i + 1)[2:]
        itemDict = dict()
        openNumbers = Lottery.db.session.query(
            func.count(
                case([
                    (Lottery.OpenNumber.data_qiou == '0:5', '0:5')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_qiou == '1:4', '1:4')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_qiou == '2:3', '2:3')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_qiou == '3:2', '3:2')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_qiou == '4:1', '4:1')
                ])),
            func.count(
                case([
                    (Lottery.OpenNumber.data_qiou == '5:0', '5:0')
                ])),
        ).filter(Lottery.OpenNumber.data_period.like("%" + dateItem + "%") if dateItem is not None else "").all()
        itemDict['date'] = dateItem
        itemDict['0:5'] = openNumbers[0][0]
        itemDict['1:4'] = openNumbers[0][1]
        itemDict['2:3'] = openNumbers[0][2]
        itemDict['3:2'] = openNumbers[0][3]
        itemDict['4:1'] = openNumbers[0][4]
        itemDict['5:0'] = openNumbers[0][5]
        list.append(itemDict)
    return list


class DataDayTypesCount(object):
    def __init__(self, date, M0, M1, M2, M3, M4):
        self.date = date
        self.M0 = M0
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3
        self.M4 = M4


def getOpenNumbers(numbers):
    dataDict = []
    list2json = {}
    for item in numbers:
        dataForecast = DataDayTypesCount(item['date'], item['m0'], item['m1'], item['m2'], item['m3'], item['m4'])
        dataDict.append(dataForecast)
    if dataDict:
        list2json["status"] = 200
        list2json["msg"] = "获取成功"
    else:
        list2json["status"] = 666
        list2json["msg"] = "没有数据啦"

    list2json["data"] = dataDict
    jsonRes = json.dumps(list2json, default=lambda obj: obj.__dict__)
    # print(jsonRes)
    return jsonRes


class DataDayDxbCount(object):
    def __init__(self, date, item05, item14, item23, item32, item41, item50):
        self.date = date
        self.item05 = item05
        self.item14 = item14
        self.item23 = item23
        self.item32 = item32
        self.item41 = item41
        self.item50 = item50


def getOpenDxbNumbers(numbers):
    dataDict = []
    list2json = {}
    for item in numbers:
        dataForecast = DataDayDxbCount(item['date'], item['0:5'], item['1:4'], item['2:3'], item['3:2'], item['4:1'],
                                       item['5:0'])
        dataDict.append(dataForecast)
    if dataDict:
        list2json["status"] = 200
        list2json["msg"] = "获取成功"
    else:
        list2json["status"] = 666
        list2json["msg"] = "没有数据啦"

    list2json["data"] = dataDict
    jsonRes = json.dumps(list2json, default=lambda obj: obj.__dict__)
    return jsonRes


def get10DayTypesCount():
    return getOpenNumbers(getDayTypesCount())


def getDayDxbCounts():
    return getOpenDxbNumbers(getDayDxbCount())


def getDayQobCounts():
    return getOpenDxbNumbers(getDayQobCount())


def getDate(day):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=day)
    n_days = now - delta
    return n_days.strftime('%Y%m%d')


if __name__ == '__main__':
    pass
    # print(getOpenNumbers(getDayTypesCount()))
    # print(getOpenDxbNumbers(getDayDxbCount()))
    # print(getOpenDxbNumbers(getDayQobCount()))
    # getDate()
