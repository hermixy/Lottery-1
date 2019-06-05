# -*- coding: UTF-8 -*-
# !/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json
import random
import DataCombinations
import Lottery
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def getData():
    try:
        request = requests.get("https://chart.ydniu.com/trend/syx5sd/")
        html_text = request.text

        dataList = []
        soup = BeautifulSoup(html_text, 'html.parser')
        trend = soup.find('div', attrs={'id': 'trend'})
        tbody = trend.find('tbody')
        # print(tbody)
        tr_list = tbody.find_all('tr')
        for tr in tr_list:
            # print(tr)
            td = tr.find_all('td')
            data_period = td[0].text
            data_award = td[1].text + " " + td[2].text + " " + td[3].text + " " + td[4].text + " " + td[5].text
            qozh_list = tr.find_all('td', attrs={'class': 'k lan2'})
            o = qozh_list[0].text  # 偶数个数
            h = qozh_list[1].text  # 合数个数
            dx_list = tr.find_all('td', attrs={'class': 'k lan21'})
            x = dx_list[0].text  # 大数个数
            d = 5 - int(x)  # 小数个数
            q = 5 - int(o)  # 奇数个数
            z = 5 - int(h)  # 质数个数
            qob = str(o) + ":" + str(q)
            dxb = str(x) + ":" + str(d)
            zhb = str(h) + ":" + str(z)
            print("期号：", data_period, " 开奖号码: ", data_award,
                  " 大小比：", dxb, " 奇偶比：", qob,
                  " 质合比：", zhb)
            itemDicts = dict()
            itemDicts["data_period"] = data_period
            itemDicts["data_award"] = data_award
            itemDicts["data_size"] = dxb
            itemDicts["data_qiou"] = qob
            itemDicts["data_zhihe"] = zhb
            dataList.append(itemDicts)
        lastNumber = Lottery.OpenNumber.query.order_by(Lottery.OpenNumber.data_period.desc()).first()
        data_period = 0
        data_type = ""
        if lastNumber:
            data_period = lastNumber.data_period
        for itemDict in dataList:
            data_period_item = itemDict['data_period']
            if int(data_period_item) > int(data_period):
                print('data_period_item: ', data_period_item, "data_period", int(data_period))
                if data_period != 0:
                    pre = str(int(data_period_item) - 1)  # 上一期
                    for item in dataList:
                        if pre == item['data_period']:
                            data_type = DataCombinations.getNumberType(itemDict['data_award'], item['data_award'])

                openNumber = Lottery.OpenNumber(data_period_item, itemDict['data_award'], data_type,
                                                "", "", itemDict['data_size'],
                                                itemDict['data_qiou'], itemDict['data_zhihe'])
                Lottery.db.session.add(openNumber)
        Lottery.db.session.commit()
    except Exception as e:
        print(e)
    finally:
        print("getData ------end------ ")


class DataAward(object):
    def __init__(self, data_period, data_award, data_type, data_value, data_span, data_size, data_qiou, data_zhihe):
        self.data_period = data_period
        self.data_award = data_award
        self.data_type = data_type
        self.data_value = data_value
        self.data_span = data_span
        self.data_size = data_size
        self.data_qiou = data_qiou
        self.data_zhihe = data_zhihe


numberDict = []


def getOpenNumbers(openNumber):
    numberDict.clear()
    list2json = {}
    # print(type(openNumber))
    for item in openNumber:
        dataAward = DataAward(item.data_period, item.data_award, item.data_type, item.data_value,
                              item.data_span, item.data_size, item.data_qiou, item.data_zhihe)
        numberDict.append(dataAward)
        # print(json.dumps(dataAward, default=lambda obj: obj.__dict__))
    if numberDict:
        list2json["status"] = 200
        list2json["msg"] = "获取成功"
    else:
        list2json["status"] = 666
        list2json["msg"] = "没有数据啦"

    list2json["listData"] = numberDict
    jsonRes = json.dumps(list2json, default=lambda obj: obj.__dict__)
    return jsonRes


def getRandom():
    return random.randint(10, 30)


def start():
    scheduler.add_job(getData, 'interval', minutes=20, id='job_index')


def stop():
    scheduler.remove_job('job_index')


if __name__ == '__main__':
    getData()
    scheduler.add_job(getData, 'interval', minutes=20, id='job_index')
    scheduler.add_job(start, 'cron', hour=9, minute=2, second=getRandom())
    scheduler.add_job(stop, 'cron', hour=23)
    scheduler.start()
