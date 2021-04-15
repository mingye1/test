#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'ming'

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG =os.path.join(BASE_DIR,"database","config.ini")
# print('TEST_CONFIG:'+TEST_CONFIG)
# 测试用例模板文件
# SOURCE_FILE = os.path.join(BASE_DIR,"database","DemoAPITestCase.xlsx")
SOURCE_FILE = os.path.join(BASE_DIR,"database","Proa_customer.xlsx")
SOURCE_FILE_2 = os.path.join(BASE_DIR,"database","PROA_H5_ATIB01.xlsx")
SOURCE_FILE_3 = os.path.join(BASE_DIR,"database","PROA_H5_ATRB03.xlsx")
SOURCE_FILE_4 = os.path.join(BASE_DIR,"database","KeHuGuanLi.xlsx")

# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","DemoAPITestCase.xlsx")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"testcase")

