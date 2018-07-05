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
    for i in range(5):
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
    print(jsonRes)
    return jsonRes

def get5DayTypesCount():
    return getOpenNumbers(getDayTypesCount())

def getDate(day):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=day)
    n_days = now - delta
    return n_days.strftime('%Y%m%d')


if __name__ == '__main__':
    getOpenNumbers(getDayTypesCount())
    # getDate()
