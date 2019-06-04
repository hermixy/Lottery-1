# -*- coding: UTF-8 -*-
# !/usr/bin/python3
import requests
from bs4 import BeautifulSoup


def getData():
    request = requests.get("https://chart.ydniu.com/trend/syx5sd/")
    html_text = request.text

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
        qob = str(q) + ":" + str(o)
        dxb = str(d) + ":" + str(x)
        zhb = str(z) + ":" + str(h)
        print("期号：", data_period, " 开奖号码: ", data_award,
              " 大小比：", dxb, " 奇偶比：", qob,
              " 质合比：", zhb)


if __name__ == '__main__':
    getData()
