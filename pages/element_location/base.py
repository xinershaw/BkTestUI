# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from selenium.webdriver.common.by import By

login = {
    u'用户名': (By.ID, 'Account'),
    u'密码': (By.ID, 'Password'),
    u'提交': (By.ID, 'btnLogin')
}

menu = {
    u'系统管理': {
        u'父菜单': (By.LINK_TEXT, u'系统管理'),
        u'角色管理': (By.LINK_TEXT, u'角色管理'),
        u'人员管理': (By.LINK_TEXT, u'人员管理')
    },
    u'配送管理':{
        u'父菜单': (By.LINK_TEXT, u'配送管理'),
        u'配送订单': (By.LINK_TEXT, u'配送订单'),
        u'配送车辆类型': (By.LINK_TEXT, u'配送车辆类型'),
        u'配送车辆信息': (By.LINK_TEXT, u'配送车辆信息'),
        u'配送司机信息': (By.LINK_TEXT, u'配送司机信息'),
    },
    u'仓储管理': {
        u'父菜单': (By.LINK_TEXT, u'仓储管理'),
        u'入库订单': (By.LINK_TEXT, u'配送仓'),
        u'配送仓': (By.LINK_TEXT, u'配送仓'),
    },
    u'用户管理': {
        u'父菜单': (By.LINK_TEXT, u'用户管理'),
        u'单纯仓配入库方': (By.LINK_TEXT, u'单纯仓配入库方'),
        u'仓储服务商': (By.LINK_TEXT, u'仓储服务商'),
        u'配送承运商': (By.LINK_TEXT, u'配送承运商')
         },
    u'平台基础信息': {
        u'父菜单': (By.LINK_TEXT, u'平台基础信息'),
        u'商品基础数据库':(By.LINK_TEXT, u'商品基础数据库'),
        u'企业信息': (By.LINK_TEXT, u'企业信息'),
        },
    u'单纯仓配': {
        u'父菜单': (By.LINK_TEXT, u'单纯仓配'),
        u'商品信息': (By.LINK_TEXT, u'商品信息'),
    },
}

tab = {
    u'首页': (By.XPATH, "//*[@id='page-wrapper']/div[2]/nav/div/a[1]"),  # 首页选项卡
    u'配送订单':{
        u'配送订单': (By.XPATH, "//a[contains(@data-id,'/distributionmanage/deliverorder')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/distributionmanage/deliverorder')]/i")
    },
    u'入库订单':{
        u'入库订单': (By.XPATH, "//a[contains(@data-id,'/storagemanage/inorder')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/storagemanage/inorder')]/i")
    },
    u'配送仓':{
        u'配送仓': (By.XPATH, "//a[contains(@data-id,'/simplestorage/warehouse')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/simplestorage/warehouse')]/i")
    },
    u'单纯仓配入库方': {
        u'单纯仓配入库方': (By.XPATH, "//a[contains(@data-id,'/usermanage/goodsowner')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/usermanage/goodsowner')]/i")
    },
    u'单纯仓配收货人': {
        u'单纯仓配收货人': (By.XPATH, "//a[contains(@data-id,'/usermanage/consignee')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/usermanage/consignee')]/i")
    },
    u'仓储服务商': {
        u'仓储服务商': (By.XPATH, "//a[contains(@data-id,'/usermanage/service')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/usermanage/service')]/i")
    },
    u'配送承运商': {
        u'配送承运商': (By.XPATH, "//a[contains(@data-id,'/usermanage/carrier')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/usermanage/carrier')]/i")
    },
    u'商品信息': {
        u'商品信息': (By.XPATH, "//a[contains(@data-id,'/simplestorage/goods')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/simplestorage/goods')]/i")
    },
}

frame = {
    u'首页': (By.XPATH, "//iframe[contains(@data-id,'/Home/Main')]"),
    u'配送订单': (By.XPATH, "//iframe[contains(@data-id,'/distributionmanage/deliverorder')]"),
    u'入库订单': (By.XPATH, "//iframe[contains(@data-id,'/storagemanage/inorder')]"),
    u'配送仓': (By.XPATH, "//iframeiframe[contains(@data-id,'/simplestorage/warehouse')]"),
    u'单纯仓配入库方': (By.XPATH, "//iframe[contains(@data-id,'/usermanage/goodsowner')]"),
    u'单纯仓配收货人': (By.XPATH, "//iframe[contains(@data-id,'/usermanage/consignee')]"),
    u'仓储服务商': (By.XPATH, "//iframe[contains(@data-id,'/usermanage/service')]"),
    u'配送承运商': (By.XPATH, "//iframe[contains(@data-id,'/usermanage/carrier')]"),
    u'商品信息': (By.XPATH, "//iframe[contains(@data-id,'/simplestorage/goods')]"),
    }