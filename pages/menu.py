# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from selenium.webdriver.common.by import By
from pages.element_location import base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Menu(BasePage):
    def clear_info_count(self, class_name):
        # 待处理记录条数会遮挡菜单，导致无法点击，因此点击前需要先将记录条数的display修改为none
        list_str = [
            "var labels = document.getElementsByClassName('",
            class_name,
            "');var i=0, len=labels.length;for (;i<len;i++)",
            "{document.getElementsByClassName('",
            class_name,
            "')[i].style.display = 'none';}"
        ]
        self.driver.execute_script(''.join(list_str))

    def is_dink(self, parent):  # 是否有子菜单
        try:
            if isinstance(base.menu[parent], dict):
                return False
            else:
                return True
        except BaseException as e:
            print u'is_dink报错：', parent, e

    def is_parent_visible(self, parent):  # 父菜单是否可见
        if self.is_dink(parent):
            return self.is_visible(base.menu[parent])
        else:
            return self.is_visible(base.menu[parent][u'父菜单'])

    def click_parent(self, parent):
        x_str = "//a[@title='" + parent + "']/.."
        if self.find_element(*(By.XPATH, x_str)).get_attribute('class') != 'active':  # 如果已展开则不再点击
            info_count_loc = (By.XPATH, "//span[@class='r label label-info']")
            if parent in [u'订单', u'异常及理赔'] and self.is_visible(info_count_loc):
                self.clear_info_count('r label label-info')  # 清除记录条数，否则无法点击
            if not self.is_parent_visible(parent):  # 如果不可见，则拉动滚动条到最下面
                link_obj = self.find_elements(*(By.XPATH, "//*[@id='side-menu']/li"))
                self.scroll_into_loc(link_obj[-1])
            try:
                if not self.is_dink(parent):
                    self.click(base.menu[parent][u'父菜单'])
                else:
                    self.click(base.menu[parent])
            except BaseException as e:
                print u'打开父菜单失败！', parent, e

    def click_son(self, parent, son):
        info_count_loc = (By.XPATH, "//span[@class='r label label-info pull-right']")  # 待处理记录条数的xpath
        if parent in [u'订单', u'异常及理赔'] and self.is_visible(info_count_loc):
            self.clear_info_count('r label label-info pull-right')  # 清除记录条数，否则无法点击
        if not self.is_visible(base.menu[parent][son]):  # 如果不可见，则拉动滚动条到最下面
            link_obj = self.find_elements(*(By.XPATH, "//li[@class='active']/ul/li/a"))
            self.scroll_into_loc(link_obj[-1])
        try:
            self.click(base.menu[parent][son])  # 打开子菜单
        except BaseException as e:
            print u'打开子菜单失败', son, e

    def open_the_menu(self, parent, son=''):  # 点击页面左侧菜单
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'side-menu')))
        try:
            if not son:  # 没有子菜单
                self.click_parent(parent)
                # 返回tab名称\链接href
                return self.find_element(*base.tab[parent][parent]).text
            else:  # 存在子菜单
                self.click_parent(parent)
                self.click_son(parent, son)
                # 返回tab名称\链接href
                return self.find_element(*base.tab[son][son]).text
        except BaseException as e:
            print u'打开菜单失败！', parent, son, e



