# -*- coding: UTF-8 -*-

from requests_html import HTMLSession
import requests
# import sched
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

session = HTMLSession()
scheduler = BlockingScheduler()

count = 0

def getData():
    global count
    response = session.get('http://caipiao.163.com/award/11xuan5/')
    content = response.html.find('section.main', first=True)
    body = content.find('tbody')
    itemDicts = dict()
    countLists = []
    countLists.clear()
    for tr in body:

        for tds in tr.find('td'):
            # print(tds.text)
            list = tds.find('td.start')
            for td in list:
                try:
                    period = td.attrs['data-period']
                    award = td.attrs['data-award']
                    # print("序号：" + td.text + " 期号：" + period + " 开奖号码：" + award)
                    countLists.append(td.text)
                    itemDicts[period] = award
                except KeyError as e:
                    print('except: ', e)
                # finally:
                #     print('finally')
    sortItemDict = sorted(itemDicts.keys(), reverse=False)
    countLists.sort(reverse=False)
    # print(countLists)
    for key in sortItemDict:
        print("期号：", key, " 开奖号码：", itemDicts[key])
        if not itemDicts[key]:
            count = key[-2:]
            break

    print(count)
    count = str(count)
    # if count == str(87):
    #     scheduler.remove_job('job_index')


if __name__ == '__main__':
    getData()
    # scheduler.add_job(getData, 'interval', seconds=30, id='job_index')
    # scheduler.start()
