# -*- coding: UTF-8 -*-

from sqlalchemy import Column, MetaData, String, Table
from flask_migrate import  MigrateCommand
import Lottery


def dropDB():
    Lottery.db.drop_all()


def createDB():
    Lottery.db.create_all()


Lottery.manager.add_command('db', MigrateCommand)


def upgrade():
    setattr("open_numbers", "data_type", (Column("data_type", String(10))))


if __name__ == '__main__':
    pass
    # createDB()
    # dropDB()
    Lottery.manager.run()
