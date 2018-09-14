# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:批量执行测试用例
"""
import unittest
import HTMLTestRunner
import datetime
import os


case_path = os.path.join(os.getcwd(), "test_case")  # 存放测试用例的路径

# 存放测试报告的文件夹
report_path = os.path.join(os.getcwd(), "test_report")
create_time = datetime.datetime.now().strftime('%Y%m%d%H%M')  # 根据年月日时分秒为测试报告命名
filename = report_path + '\TestResult' + create_time + '.html'  # 根据执行测试的日期时间为测试报告命名
fp = file(filename, 'wb')

# 加载case_path路径下的所有Test开头的py文件（测试用例）
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)

# 实例化一个HTMLTestRunner
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试结果', description='测试报告')

# 开始跑
runner.run(discover)