# -*- coding: UTF-8 -*-
# !/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json
import random
import Lottery
import schedule
import time


def getData():
    try:
        request = requests.get("https://chart.ydniu.com/Trend/Dlt/dltjbzs.html")
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

            data_award = ""
            red_list = tr.find_all('td', attrs={'class': 'hongqiu'})
            for qiu in red_list:
                n = int(qiu.text)  # 红球
                s = "%02d" % n
                data_award += s + " "

            bule_list = tr.find_all('td', attrs={'class': 'lan'})
            bule1 = bule_list[0].text  # 蓝球
            bule1 = "%02d" % int(bule1)
            data_award += bule1 + " "

            bule = bule_list[1].text  # 蓝球
            bule = "%02d" % int(bule)
            data_award += bule

            print("期号：", data_period, " 开奖号码: ", data_award)
            itemDicts = dict()
            itemDicts["data_period"] = data_period
            itemDicts["data_award"] = data_award
            dataList.append(itemDicts)

        lastNumber = Lottery.OpenNumber_Dlt.query.order_by(Lottery.OpenNumber_Dlt.data_period.desc()).first()
        data_period = 0
        if lastNumber:
            data_period = lastNumber.data_period
        for itemDict in dataList:
            data_period_item = itemDict['data_period']
            if int(data_period_item) > int(data_period):
                openNumber = Lottery.OpenNumber_Dlt(data_period_item, itemDict['data_award'])
                Lottery.db.session.add(openNumber)

        Lottery.db.session.commit()
    except Exception as e:
        print(e)
    finally:
        print("getData ------end------ ")


class DataAward(object):
    def __init__(self, data_period, data_award):
        self.data_period = data_period
        self.data_award = data_award


numberDict = []


def getOpenNumbers(openNumber):
    numberDict.clear()
    list2json = {}
    # print(type(openNumber))
    for item in openNumber:
        dataAward = DataAward(item.data_period, item.data_award)
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


# def start():
#     scheduler.add_job(getData, 'interval', minutes=20, id='job_index')
#
#
# def stop():
#     scheduler.remove_job('job_index')


if __name__ == '__main__':
    getData()
    schedule.every().day.at("20:30").do(getData)
    while True:
        schedule.run_pending()
        time.sleep(1)
