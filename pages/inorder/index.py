# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from pages.element_location import inorder as loc
from pages.menu import Menu
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InOrder(BasePage):
    def open_page(self):
        self.login()  # 登录
        menu = Menu(self.driver)
        menu.open_the_menu(u'仓储管理', u'入库订单')  # 打开菜单
        self.to_frame(u'入库订单')  # 去到右边入库订单的frame
        time.sleep(3)  # # 强制等待页面加载

    def click_add(self):
        self.click(loc.inorder[u'新增'])



