# -*- coding: UTF-8 -*-

from requests_html import HTMLSession
# import requests
# import sched
import time
from datetime import datetime
import json
import random
from apscheduler.schedulers.blocking import BlockingScheduler
import Lottery

session = HTMLSession()
scheduler = BlockingScheduler()

count = 0
# numberDicts = dict()

def getData():
    global count
    response = session.get('http://caipiao.163.com/award/11xuan5/')
    content = response.html.find('section.main', first=True)
    body = content.find('tbody')
    itemDicts = dict()

    # countLists = []
    # countLists.clear()
    for tr in body:

        for tds in tr.find('td'):
            # print(tds.text)
            list = tds.find('td.start')
            for td in list:
                try:
                    period = td.attrs['data-period']
                    award = td.attrs['data-award']
                    # print("序号：" + td.text + " 期号：" + period + " 开奖号码：" + award)
                    # countLists.append(td.text)
                    itemDicts[period] = award
                except KeyError as e:
                    print('except: ', e)
                # finally:
                #     print('finally')
    sortItemDict = sorted(itemDicts.keys(), reverse=False)
    # print(sortItemDict)
    # print(itemDicts)
    # countLists.sort(reverse=False)
    # print(countLists)
    lastNumber = Lottery.OpenNumber.query.order_by(Lottery.OpenNumber.data_period.desc()).first()
    data_period = 0
    if lastNumber:
        data_period = lastNumber.data_period
    for key in sortItemDict:
        if not itemDicts[key]:
            count = key[-2:]
            break

        if int(key) > int(data_period):
            # numberDicts[key] = itemDicts[key]
            openNumber = Lottery.OpenNumber(key, itemDicts[key])
            Lottery.db.session.add(openNumber)

    Lottery.db.session.commit()
    # print(numberDicts)
    print(count)
    count = str(count)
    print("getData ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # if count == str(87):
    #     scheduler.remove_job('job_index')
    # return numberDicts


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
    list2json["listData"] = numberDict
    jsonRes = json.dumps(list2json, default=lambda obj: obj.__dict__)
    return jsonRes

def start():
    scheduler.add_job(getData, 'interval', minutes=10, id='job_index')
    print("start ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def stop():
    scheduler.remove_job('job_index')
    print("stop ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    # getData()
    scheduler.add_job(getData, 'interval', minutes=10, id='job_index')
    scheduler.add_job(start, 'cron', hour=8, minute=28, seconds=random.randint(1, 5))
    scheduler.add_job(stop, 'cron', hour=23)

    scheduler.start()

