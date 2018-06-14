# -*- coding: UTF-8 -*-
from itertools import combinations
from itertools import permutations
from itertools import filterfalse
import json

test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in combinations(test_data, 5):
#     number = list(i)
#     end = list(filterfalse(lambda x: x == 1 and x == 2, number))
#     print(end)

# def is_same(x) :
#     return x == 1 or x == 2;

listsOf0 = []
listsOf1 = []
listsOf2 = []
listsOf3 = []
listsOf4 = []

logOpen = False


def calculate(numbers):
    listsOf0.clear()
    listsOf1.clear()
    listsOf2.clear()
    listsOf3.clear()
    listsOf4.clear()
    open_number = set(numbers)
    for a in combinations(test_data, 5):
        start = set(a)
        # print("a ", start)
        # print("交集： ", start & open_number)
        if start & open_number:
            count = len(start & open_number)
            if count == 1:
                listsOf1.append(start)
            elif count == 2:
                listsOf2.append(start)
            elif count == 3:
                listsOf3.append(start)
            elif count == 4:
                listsOf4.append(start)
            # print(print("最终包含： ", set(a)))
        else:
            listsOf0.append(set(a))
            # print("没有交集", set(a))

    if logOpen:
        print("M0: ", len(listsOf0), "组 ", listsOf0)
        print("M1: ", len(listsOf1), "组 ", listsOf1)
        print("M2: ", len(listsOf2), "组 ", listsOf2)
        print("M3: ", len(listsOf3), "组 ", listsOf3)
        print("M4: ", len(listsOf4), "组 ", listsOf4)


def initNumbers(strs):
    str_list = strs.strip(',').split(',')
    new_list = []
    for number in str_list:
        n = int(number)
        s = "%01d" % n
        new_list.append(int(s))
    # list.sort(reverse=False)
    calculate(new_list)


class DataForecast(object):
    def __init__(self, number):
        self.number = number


numberDict = []


def getOpenNumbers(numbers):
    numberDict.clear()
    list2json = {}
    for item in numbers:
        l = list(item)
        for i in range(0, l.__len__()):
            l[i] = str(l[i])
        s = ','.join(l)
        dataForecast = DataForecast(s)
        numberDict.append(dataForecast)

    list2json["listData"] = numberDict
    jsonRes = json.dumps(list2json, default=lambda obj: obj.__dict__)
    return jsonRes


def getForecastNumbers(method, numbers):
    initNumbers(numbers)
    if method == str("m0"):
        return getOpenNumbers(listsOf0)
    if method == str("m1"):
        return getOpenNumbers(listsOf1)
    if method == str("m2"):
        return getOpenNumbers(listsOf2)
    if method == str("m3"):
        return getOpenNumbers(listsOf3)
    if method == str("m4"):
        return getOpenNumbers(listsOf4)


if __name__ == '__main__':
    strs = "04,01,10,03,09"
    initNumbers(strs)
    print(getOpenNumbers(listsOf0))
