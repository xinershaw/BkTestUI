# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from selenium.common.exceptions import StaleElementReferenceException as SERE


class SearchForm(BasePage):
    def combined_query(self, *test_data, **loc):  # 组合查询 loc是指定位器中的字典变量
        self.input_items(*test_data, **loc)
        self.click(loc[u'搜索'])

    def single_query(self, item_input, item_name, **loc):  # 单一查询 loc是指定位器中的字典变量
        if item_name in loc[u'查询条件']['select']:
            self.select_value(item_input, *loc[u'查询条件']['select'][item_name])
        elif item_name in loc[u'查询条件']['input_search']:
            self.input_search(item_input, **loc[u'查询条件']['input_search'][item_name])
        else:
            self.send_keys(item_input, *loc[u'查询条件']['input'][item_name])
        self.click(loc[u'搜索'])

    def get_line1(self, **loc):  # 到货分理列表，获取列表第一行数据的运单号 loc是指定位器中的字典变量
        line1 = dict()
        heads = []
        values = []
        for i in range(1, len(self.find_elements(*loc[u'列表'][u'表头']))):
            try:
                heads.append(self.find_elements(*loc[u'列表'][u'表头'])[i].text)
            except SERE:
                heads.append(self.find_elements(*loc[u'列表'][u'表头'])[i].text)
        for i in range(0, len(self.find_elements(*loc[u'列表'][u'第一行所有数据']))):
            values.append(self.find_elements(*loc[u'列表'][u'第一行所有数据'])[i].text)
        for head, value in zip(heads, values):
            line1.update({head: value})
        return line1
