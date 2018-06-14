# -*- coding: UTF-8 -*-

import Lottery

def dropDB():
    Lottery.db.drop_all()

def createDB():
    Lottery.db.create_all()

if __name__ == '__main__':
    pass
    # createDB()
    # dropDB()