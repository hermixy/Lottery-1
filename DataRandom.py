# -*- coding: UTF-8 -*-
# !/usr/bin/python3

import random
import json


def randoms(type):
    number = ""
    if type == "ssq":
        red = generate_num(6, 1, 33)
        blue = generate_num(1, 1, 16)
        number = "红球：" + red + " 蓝球：" + blue
    elif type == "dlt":
        red = generate_num(5, 1, 35)
        blue = generate_num(2, 1, 12)
        number = "红球：" + red + " 蓝球：" + blue
    elif type == "fc3d" or type == "pl3":
        bai = generate_num(1, 0, 9)
        shi = generate_num(1, 0, 9)
        ge = generate_num(1, 0, 9)
        number = "百位：" + bai + " 十位：" + shi + " 个位：" + ge
    elif type == "pl5":
        wan = generate_num(1, 0, 9)
        qian = generate_num(1, 0, 9)
        bai = generate_num(1, 0, 9)
        shi = generate_num(1, 0, 9)
        ge = generate_num(1, 0, 9)
        number = "万位：" + wan + " 千位：" + qian + " 百位：" + bai + " 十位：" + shi + " 个位：" + ge
    elif type == "qxc":
        one = generate_num(1, 0, 9)
        two = generate_num(1, 0, 9)
        three = generate_num(1, 0, 9)
        four = generate_num(1, 0, 9)
        five = generate_num(1, 0, 9)
        six = generate_num(1, 0, 9)
        seven = generate_num(1, 0, 9)
        number = one + " " + two + " " + three + " " + four + " " + five + " " + six + " " + seven
    elif type == "qlc":
        red = generate_num(7, 1, 30)
        blue = generate_num(1, 1, 30)
        number = "红球：" + red + " 蓝球：" + blue
    print(number)
    return number


def random_num(type, count):
    numbers = []
    for i in range(count):
        num_str = randoms(type)
        numbers.append(num_str)
    return numbers


def generate_num(count, start_number, end_number):
    lists = random.sample(range(start_number, end_number + 1), count)
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
    numbers = random_num(type, int(count))
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
    get_jx_numbers("qlc", "5000")
