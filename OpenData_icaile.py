# -*- coding: UTF-8 -*-

from requests_html import HTMLSession
import time
from datetime import datetime
import json
import random
import base64
from apscheduler.schedulers.blocking import BlockingScheduler
import Lottery
import DataCombinations
import requests
from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

session = HTMLSession()
scheduler = BlockingScheduler()


# IS_CENTOS = False

# numberDicts = dict()

def getData():
    print("getData -----start------- ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # if IS_CENTOS:
    #     # CentOS 兼容配置开始-------------------------------#
    #     options = Options()
    #     options.add_argument('--headless')
    #     options.add_argument('--no-sandbox')
    #     # options.add_argument('--disable-dev-shm-usage')
    #     browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=options)
    #     # CentOS 兼容配置结束-------------------------------#
    # else:
    #     browser = webdriver.Chrome()
    #
    # browser.get("http://sd11x5.icaile.com/")
    # html_text = browser.page_source
    try:
        request = requests.get("http://sd11x5.icaile.com/")
        html_text = request.text
        # print(html_text)

        dataList = []
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', attrs={'class': 'fixedtable'})
        # print(table)
        # tbody = table.find('tbody')
        # print(tbody)
        body = table.find_all('tr')
        # print(body)
        # countLists = []
        # countLists.clear()

        for tr in body:
            # print(tr)
            tds = tr.find_all('td')
            data_period = tr.find('td', attrs={'class', 'chart-bg-qh'})
            if data_period:
                data_award_s = tr.find_all('td', attrs={'class', 'cc'})
                index = 0
                period_str = ''
                for period in data_award_s:
                    if index > 0:
                        period_str = period_str + ' '
                    s = base64.b64decode(str(period.get_text()[1:-1])).decode('utf-8')
                    period_str += s
                    index += 1
                # print("期号：", data_period.get_text(), "开奖号码: ", period_str, "和值：", tds[22].get_text(),
                #       "跨度：", tds[23].get_text(), "大小比：", tds[24].get_text(), "奇偶比：", tds[25].get_text(),
                #       "质合比：", tds[26].get_text())
                itemDicts = dict()
                itemDicts["data_period"] = data_period.get_text()
                itemDicts["data_award"] = period_str
                itemDicts["data_value"] = tds[22].get_text()
                itemDicts["data_span"] = tds[23].get_text()
                itemDicts["data_size"] = tds[24].get_text()
                itemDicts["data_qiou"] = tds[25].get_text()
                itemDicts["data_zhihe"] = tds[26].get_text()
                dataList.append(itemDicts)
        # print(dataList)
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
                                                itemDict['data_value'], itemDict['data_span'], itemDict['data_size'],
                                                itemDict['data_qiou'], itemDict['data_zhihe'])
                Lottery.db.session.add(openNumber)
        Lottery.db.session.commit()
    except KeyError as e:
        print(e)
    finally:
        print("getData ------end------ ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class DataAward(object):
    def __init__(self, data_period, data_award, data_type):
        self.data_period = data_period
        self.data_award = data_award
        self.data_type = data_type


numberDict = []


def getOpenNumbers(openNumber):
    numberDict.clear()
    list2json = {}
    # print(type(openNumber))
    for item in openNumber:
        dataAward = DataAward(item.data_period, item.data_award, item.data_type)
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
    return random.randint(10, 20)


def start():
    scheduler.add_job(getData, 'interval', minutes=10, id='job_index')
    print("start ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def stop():
    scheduler.remove_job('job_index')
    print("stop ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    getData()
    # scheduler.add_job(getData, 'interval', minutes=10, id='job_index')
    # scheduler.add_job(start, 'cron', hour=8, minute=27, second=getRandom())
    # scheduler.add_job(stop, 'cron', hour=23)
    #
    # scheduler.start()
