# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from selenium.webdriver.common.by import By


class AreaController(BasePage):
    def click_area(self, area_tab_loc, area_name):
        if self.find_element(*area_tab_loc).get_attribute('class') == 'active':  # 如果需要的tab没被选中，则点击选中
            self.click(area_tab_loc)
        area_name_loc = (By.LINK_TEXT, area_name)  # 地名在控件中的定位
        self.click(area_name_loc)

    def open_controller(self, *input_loc):
        # 弹出地区控件的触发事件是input的focus，但被下面的span干扰，无法通过点击实现，只能通过js聚焦实现
        if 'id' in input_loc[0]:  # 如果地区控件是通过id定位,
            js = "document.getElementById('" + input_loc[1] + "').focus()"
        else:  # 如果地区控件是通过name定位
            js = "document.getElementsByName('" + input_loc[1] + "')[0].focus()"
        self.driver.execute_script(js)  # 弹出地区控件

    def input_area(self, *input_loc, **test_data):
        self.open_controller(*input_loc)
        # div_xpath是由于一个页面包含多个地区控件时，能区分各个控件的省市区乡tab的xpath
        div_xpath = "//div[@class='city-picker-dropdown' and contains(@style,'block')]/div/div/a[@data-count='"
        try:
            for i in ['province', 'city', 'district', 'county']:
                try:
                    self.click_area((By.XPATH, div_xpath + i + "']"), test_data[i])
                except KeyError:  # 有的控件不包含county,这种情况下，testdata不设置键值对'county'
                    continue
        except BaseException as e:
            print input_loc, '地区控件选择地区失败！', e

    def input_clear(self, *input_loc):  # 地区控件中的清空按钮
        self.open_controller(*input_loc)
        self.click((By.XPATH, "//div[@class='city-picker-dropdown' and contains(@style,'block')]/div/div/input"))
