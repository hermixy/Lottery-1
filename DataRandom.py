# -*- coding: UTF-8 -*-
# !/usr/bin/python3

import random
import json


def randoms(type):
    number = ""
    if type == "ssq":
        red = generate_num(6, 33)
        blue = generate_num(1, 16)
        number = "红球：" + red + " 蓝球：" + blue
    elif type == "dlt":
        red = generate_num(5, 35)
        blue = generate_num(2, 12)
        number = "红球：" + red + " 蓝球：" + blue
    return number


def random_num(type, count):
    numbers = []
    for i in range(count):
        num_str = randoms(type)
        numbers.append(num_str)
    return numbers


def generate_num(count, end_number):
    lists = random.sample(range(1, end_number), count)
    lists.sort(reverse=False)
    numbers = ''
    for index in range(len(lists)):
        if index > 0:
            numbers += " "
        numbers += "%02d" % lists[index]

    return numbers


class JxData(object):
    def __init__(self, number):
        self.number = number


def get_jx_numbers(type, count):
    numberDict = []
    list2json = {}
    numbers = random_num(type, count)
    for item in numbers:
        data = JxData(item)
        numberDict.append(data)
    if numberDict:
        list2json["status"] = 200
        list2json["msg"] = "获取成功"
    else:
        list2json["status"] = 666
        list2json["msg"] = "没有数据啦"

    list2json["listData"] = numberDict
    jsonRes = json.dumps(list2json, default=lambda obj: obj.__dict__)
    print(jsonRes)
    return jsonRes


if __name__ == '__main__':
    # random_num("dlt", 3)
    get_jx_numbers("ssq", 3)
