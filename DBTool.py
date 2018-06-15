# -*- coding: UTF-8 -*-

from sqlalchemy import Column, MetaData, String, Table
from flask_sqlalchemy import declarative_base
import Lottery

Base = declarative_base()

def dropDB():
    Lottery.db.drop_all()

def createDB():
    Lottery.db.create_all()

def upgrade():
    setattr("open_numbers", "data_type", (Column("data_type", String(10))))

if __name__ == '__main__':
    # pass
    createDB()
    # dropDB()