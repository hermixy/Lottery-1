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
    # return new_list


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
        s = ' '.join(l)
        dataForecast = DataForecast(s)
        numberDict.append(dataForecast)
    if numberDict:
        list2json["status"] = 200
        list2json["msg"] = "获取成功"
    else:
        list2json["status"] = 666
        list2json["msg"] = "没有数据啦"

    list2json["listData"] = numberDict
    jsonRes = json.dumps(list2json, default=lambda obj: obj.__dict__)
    # print(jsonRes)
    return jsonRes


# 类型 开奖号码 筛选类型 筛除号码 定胆号码 筛除大小比 筛除奇偶比
def getForecastNumbers(method, numbers, scNumber, ddNumber, dxbNumber, qobNumber):
    initNumbers(numbers)
    if method:
        resultList = []
        sxList0 = []
        sxList1 = []
        sxList2 = []
        sxList3 = []
        sxList4 = []
        types = method.strip(',').split(',')
        for type in types:
            if type == str("m0"):
                sxList0 = setSxResultList(ddNumber, scNumber, dxbNumber, qobNumber, listsOf0)
            elif type == str("m1"):
                sxList1 = setSxResultList(ddNumber, scNumber, dxbNumber, qobNumber, listsOf1)
            elif type == str("m2"):
                sxList2 = setSxResultList(ddNumber, scNumber, dxbNumber, qobNumber, listsOf2)
            elif type == str("m3"):
                sxList3 = setSxResultList(ddNumber, scNumber, dxbNumber, qobNumber, listsOf3)
            elif type == str("m4"):
                sxList4 = setSxResultList(ddNumber, scNumber, dxbNumber, qobNumber, listsOf4)

        setSxList(sxList0, resultList)
        setSxList(sxList1, resultList)
        setSxList(sxList2, resultList)
        setSxList(sxList3, resultList)
        setSxList(sxList4, resultList)
        # print(len(resultList), "组 ", resultList)

        return getOpenNumbers(resultList)


def setSxList(sxList, resultList):
    for sxListItem in sxList:
        resultList.append(sxListItem)


#  筛除号码
def setSxScNumber(scNumber, list):
    resultList = []
    scNumberSet = calculateNumber(scNumber)  # 筛除号码
    if not scNumberSet:
        return list
    else:
        for itemList in list:
            if not itemList & scNumberSet:
                # print(itemList)
                resultList.append(itemList)
        return resultList


# 筛选定胆号码
def setSxDdNumber(ddNumber, list):
    resultList = []
    ddNumberSet = calculateNumber(ddNumber)  # 定胆号码
    if not ddNumberSet:
        return list
    else:
        for itemList in list:
            if itemList & ddNumberSet:
                # print(itemList)
                resultList.append(itemList)
        return resultList


# 筛除大小比号码
def setSxDxbNumber(dxbNumber, list):
    resultList = []
    if not dxbNumber:
        return list
    else:
        return resultList


# 筛除奇偶比号码
def setSxDxbNumber(qobNumber, list):
    resultList = []
    if not qobNumber:
        return list
    else:
        for itemList in list:
            for item in itemList:
                if int(item) % 2 == 0:
                    print("{0} 是偶数".format(int(item)))
                else:
                    print("{0} 是奇数".format(int(item)))
        return resultList


# 根据规则筛除号码
def setSxResultList(ddNumber, scNumber, dxbNumber, qobNumber, listOf):
    scResultList = setSxScNumber(scNumber, listOf)  # 筛除后的号码
    ddResultList = setSxDdNumber(ddNumber, scResultList)  # 用筛除后的号码筛选定胆号码
    dxbResultList = setSxDxbNumber(dxbNumber, ddResultList)
    qobbResultList = setSxDxbNumber(qobNumber, dxbResultList)
    return qobbResultList


def calculateNumber(numbers):
    start_new_list = []
    if numbers:
        start_list = numbers.split(' ')
        for number in start_list:
            n = int(number)
            s = "%01d" % n
            start_new_list.append(int(s))
        # list.sort(reverse=False)
    return set(start_new_list)


def getNumberType(start, end):
    start_set = calculateNumber(start)
    end_set = calculateNumber(end)
    count = getIntersectionNum(start_set, end_set)
    if count == 1:
        return "M1"
    elif count == 2:
        return "M2"
    elif count == 3:
        return "M3"
    elif count == 4:
        return "M4"
    else:
        return "M0"


# 得到并集数
def getIntersectionNum(start, end):
    return len(start & end)


if __name__ == '__main__':
    strs = "04,05,10,09,07"
    # initNumbers(strs)
    # print(getNumberType("1 03 9", "04 01 10 03 09"))
    # print(calculateNumber("1 03 9"))
    # print(getOpenNumbers(listsOf0))
    getForecastNumbers("m3,m2", strs, "04", "05 07", "", "")
