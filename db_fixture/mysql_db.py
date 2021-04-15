#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'ming'

import os
import sys
# import pymysql
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from pymysql import connect, cursors
from pymysql.err import OperationalError
import configparser as cparser

# --------- 读取config.ini配置文件 ---------------
cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG, encoding='UTF-8')
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
db = cf.get("mysqlconf", "db_name")


class DB:
    """
    MySQL基本操作
    """

    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8',
                                cursorclass=cursors.DictCursor
                                )
            print("链接成功！")
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # # 清除表数据
    # def clear(self, table_name):
    #     real_sql = "delete from " + table_name + ";"
    #     with self.conn.cursor() as cursor:
    #         # 取消表的外键约束
    #         cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    #         cursor.execute(real_sql)
    #     self.conn.commit()

    # # 插入表数据
    # def insert(self, table_name, table_data):
    #     for key in table_data:
    #         table_data[key] = "'" + str(table_data[key]) + "'"
    #     key = ','.join(table_data.keys())
    #     value = ','.join(table_data.values())
    #     real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
    #
    #     with self.conn.cursor() as cursor:
    #         cursor.execute(real_sql)
    #     self.conn.commit()
    def select(self):
        print(777777777777777777777777777777777)
    # 关闭数据库
    def close(self):
        self.conn.close()

    # 初始化数据
    # def init_data(self, datas):
    #     print('6666666666666666666666666666666666666666666666666')
    #     for table, data in datas.items():
    #         self.clear(table)
    #         for d in data:
    #             self.insert(table, d)
    #     self.close()

    # 初始化数据
    def init_data(self):
        self.db()
        print('6666666666666666666666666666666666666666666666666')
        self.select()
        self.close()


if __name__ == '__main__':
    DB()