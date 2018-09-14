# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from pages.inorder.index import InOrder
from pages.element_location import inorder as loc
from pages.menu import Menu
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InOrderAdd(BasePage):
    def input_base_info(self):
        pass

    def input_good_info(self):
        pass

    def add_goods_alert(self):
        pass

    def submit_order(self):
        inorder = InOrder(self.driver)
        inorder.open_page()
        inorder.click_add()
        self.input_base_info()
        self.input_good_info()
        self.click(loc.inorder_add[u'提交'])

