# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from selenium.webdriver.common.by import By


inorder = {
    u'新增': (By.ID, 'add-order'),
    u'查询条件': {
        'input': {
            u'订单号': (By.NAME, 'OrderNo'),
        },
        'select': {
            u'订单状态': (By.ID, 'Status')
        },
        'input_search': {
            u'仓库': {  # 固定格式
                'input': (By.ID, 'WarehouseName'),
                'item': (By.XPATH, "//*[@id='searchForm']/div[2]/div/ul/table/tbody/tr[1]")
            },
            u'所属入库方': {  # 固定格式
                'input': (By.ID, 'GoodsOwnerName'),
                'item': (By.XPATH, "//*[@id='searchForm']/div[1]/div/ul/table/tbody/tr[1]")
                    }
        },
    },
    u'搜索': (By.ID, 'btn_search'),
    u'重置': (By.XPATH, "//*[@id='searchForm']/div[8]/button[2]"),
    u'列表': {
        u'整体': (By.ID, 'tablelist'),
        u'表头': (By.XPATH, "//*[@id='tablelist']/table/thead/tr"),
        u'第一行': (By.XPATH, "//*[@id='tablelist']/table/tbody/tr[1]"),
        u'第一行所有数据': (By.XPATH, "//*[@id='tablelist']/table/tbody/tr[1]/td/span")
    },
}

inorder_add = {
    'input_search': {
        u'入库方': {  # 固定格式
                'input': (By.ID, 'GoodsOwnerName'),
                'item': (By.XPATH, "//*[@id='inorderForm']/div/div[2]/div/div/div[1]/div/ul/table/tbody/tr[1]")
                  }
    },
    u'批量添加按钮': (By.ID, 'batch-goods-btn'),
    u'批量添加弹窗':{
        u'整体': (By.ID, 'layui-layer3'),
        u'第一行数据': (By.XPATH, "//*[@id='batch-goodslist']/table/tbody/tr[1]/td/span"),
        u'保存': (By.ID, "bath-goods-save-btn")
    },
    u'提交': (By.ID, 'btnSave')

}