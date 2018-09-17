# coding=utf-8
"""
Created on 2018年8月29日
@author: Xiaoxin
Project:......
"""
import unittest
from selenium import webdriver
from pages import menu
from pages.element_location import base
import time


class CaseMenu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def assert_page_source(self, menu_name, page_source):
        try:
            key_word = [u'服务器错误', u'未将对象引用到', 'Not Found', 'InnerError', u'系统异常', 'noright', 'NoRight']
            self.assertNotIn(key_word, page_source)
        except AssertionError as e:
            print menu_name, u'打开此页面报错！', e

    def assert_tab_name(self, menu_name, tab_name):
        try:
            self.assertEqual(menu_name, tab_name)
        except AssertionError as e:
            print menu_name, u'打开此菜单的tab页测试不通过！', e

    def test_open_menus(self):  # 新增到货分理-冒烟测试
        page = menu.Menu(self.driver)
        page.login()
        menus = base.menu
        for parent in menus:
            # 如果是dict，说明有子菜单,反之则没有子菜单
            if not page.is_dink(parent):
                for son in menus[parent]:
                    if son != u'父菜单':
                        tab_name = page.open_the_menu(parent, son)  # 打开菜单
                        time.sleep(1)
                        page.to_frame(son)
                        page_source = page.driver.page_source
                        self.driver.switch_to.default_content()  # 从frame中出来，否则定位不到tab
                        page.close_tab(son)
                        self.assert_page_source(son, page_source)
                        self.assert_tab_name(son, tab_name)
            else:  # 没有二级菜单的情况
                tab_name = page.open_the_menu(parent)
                time.sleep(1)
                page.to_frame(parent)
                page_source = page.driver.page_source
                self.driver.switch_to.default_content()
                page.close_tab(parent)
                self.assert_page_source(parent, page_source)
                self.assert_tab_name(parent, tab_name)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()