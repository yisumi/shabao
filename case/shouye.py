# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""说明：“首页”模块测试用例。"""
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.public import ShaBao
from time import sleep
from casedata.basicdata import data_login

account = data_login["account"]
password = data_login["password"]


class ShouYe(ShaBao):
    # 首页-》城市，定位城市选择。
    # 注意：华为mate8不适用此用例，因为无法在选择城市页面获取页面元素。
    # @unittest.skip('暂不执行用例')
    def test_001(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“城市”。
        self.cs()
        # 等待标题加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/toolbar_title")))
        # 点击“重新定位”
        self.cxdw()
        # 获取并选择该定位城市。
        city_name1 = driver.find_element_by_id("com.seebon.shabaomanager:id/located_city_tv").get_attribute("name")
        print(city_name1)
        driver.find_element_by_id("com.seebon.shabaomanager:id/located_city_tv").click()
        # 获取首页的城市名称。
        city_name2 = driver.find_element_by_id("com.seebon.shabaomanager:id/toolbar_location").get_attribute("name")
        print(city_name2)
        # 判断是否成功选择城市。
        self.assertEqual(city_name2, city_name1, '功能异常')

    # 首页-》城市，热门城市选择。
    # 注意：华为mate8不适用此用例，因为无法在选择城市页面获取页面元素。
    # @unittest.skip('暂不执行用例')
    def test_002(self):
        city_name = "深圳"
        driver = self.driver
        # sleep(5)
        #WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
         #   EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/update_cancel_btn")))
        #点击“取消”
        #self.quxiaogengxin()
        # 点击“首页”。
        self.shouye()
        # 点击“城市”。
        self.cs()
        # 等待标题加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/toolbar_title")))
        sleep(5)
        # 获取并选择一个城市。
        city_name1 = "深圳"
        # 首页-》城市选择-》热门城市-》深圳，
        size = driver.get_window_size()
        width = size['width']
        height =size['height']
        X1 = 15/540
        Y1 = 386/960
        X2 = 113/540
        Y2 = 431/960
        def zuobiao(width, height):
            return[(width*X1, height*Y1), (width*X2, height*Y2)]
        print(zuobiao(width, height))
        # 三星手机，(15, 386), (113, 431)
        driver.tap(zuobiao(width, height), 500)
        # 华为mate8，
        # driver.tap([], 100)
        sleep(3)
        #driver.swipe(407, 426, 65, 426, 500)
        driver.swipe(473, 492, 131, 492, 500)
        sleep(3)
        size = driver.get_window_size()
        print(size)
        print(size['width'], size['height'])


















        # 右侧：[407,426][473,492]
        # 左侧：[65,426][131,492]
        print(city_name1)
        #driver.find_element_by_name(city_name).click()
        # 获取首页的城市名称。
        city_name2 = driver.find_element_by_id("com.seebon.shabaomanager:id/toolbar_location").get_attribute("text")
        print(city_name2)
        # 判断是否成功选择城市。
        self.assertEqual(city_name2, city_name1, '功能异常')

    # 首页-》城市，列表城市选择。
    # 注意：华为mate8不适用此用例，因为无法在选择城市页面获取页面元素。
    # @unittest.skip('暂不执行用例')
    def test_003(self):
        city_name = "鞍山"
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“城市”。
        self.cs()
        # 等待标题加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/toolbar_title")))
        # 获取并选择一个城市。
        city_name1 = driver.find_element_by_name(city_name).get_attribute("name")
        print(city_name1)
        driver.find_element_by_name(city_name).click()
        # 获取首页的城市名称。
        city_name2 = driver.find_element_by_id("com.seebon.shabaomanager:id/toolbar_location").get_attribute("name")
        print(city_name2)
        # 判断是否成功选择城市。
        self.assertEqual(city_name2, city_name1, '功能异常')

    # 首页-》城市，搜索城市选择。
    # 注意：华为mate8不适用此用例，因为无法在选择城市页面获取页面元素。
    # @unittest.skip('暂不执行用例')
    def test_004(self):
        search_name = "shanghai"
        city_name = "上海"
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“城市”。
        self.cs()
        # 等待标题加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/toolbar_title")))
        # 点击搜索框。
        driver.find_element_by_id("com.seebon.shabaomanager:id/city_search_layout").click()
        # 输入城市拼音/拼音首字母。
        driver.find_element_by_id("com.seebon.shabaomanager:id/toolbar_search_edit").send_keys(search_name)
        # 该城市中文。
        city_name1 = city_name
        print(city_name1)
        # 选择城市。
        driver.find_element_by_id("com.seebon.shabaomanager:id/tv_item_city_listview_name").click()
        # driver.find_element_by_id("com.seebon.shabaomanager:id/tv_item_province_listview_name").click()
        # 获取首页的城市名称。
        city_name2 = driver.find_element_by_id("com.seebon.shabaomanager:id/toolbar_location").get_attribute("name")
        print(city_name2)
        # 判断是否成功选择城市。
        self.assertEqual(city_name2, city_name1, '功能异常')

    # 首页-》消息中心，遍历消息中心中的模块。
    # 注意：华为mate8不适用此用例，因为无法在消息中心及其子页面获取标题。
    # @unittest.skip('暂不执行用例')
    def test_005(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“首页”。
        self.shouye()
        # 点击“消息中心”。
        self.xxzx()
        # 判断标题
        self.assertEqual(self.get_title(), "消息中心", '功能异常')

        # 点击“待办事项”。
        self.dbsx()
        # 判断标题
        self.assertEqual(self.get_title(), "待办事项", '功能异常')
        # 点击返回键。
        self.fanhui()

        # 点击“系统消息”。
        self.xtxx()
        # 判断标题
        self.assertEqual(self.get_title(), "系统消息", '功能异常')
        # 点击返回键。
        self.fanhui()

        # 点击“精彩活动”。
        self.jchd()
        # 判断标题
        self.assertEqual(self.get_title(), "精彩活动", '功能异常')
        # 点击返回键。
        self.fanhui()

        # 点击返回键。
        self.fanhui()
        # 判断标题
        self.assertEqual(self.get_title(), "首页", '功能异常')

    """
    # 首页-》首页广告，查看广告。
    #@unittest.skip('暂不执行用例')
    def test_006(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        title_name = self.get_title()
        # 点击广告。
        self.sygg()
        # 点击返回键。
        self.fanhui()
        # 获取标题，判断是否返回到首页。
        self.assertEqual(self.get_title(), title_name, '功能异常')

    """

    # 首页-》待办事项提醒，查看待办事项。
    # 注意：华为mate8不适用此用例，因为无法在消息中心及其子页面获取标题。
    # @unittest.skip('暂不执行用例')
    def test_007(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“首页”。
        self.shouye()
        title_name = self.get_title()
        # 点击“待办事项提醒”。
        self.dbsxtx()
        # 获取标题，判断是否进入待办事项页面。
        self.assertEqual(self.get_title(), "待办事项", '功能异常')
        # 点击返回键。
        self.fanhui()
        # 获取标题，判断是否返回到首页。
        self.assertEqual(self.get_title(), title_name, '功能异常')

    # 首页-》首页活动，查看首页活动。
    # @unittest.skip('暂不执行用例')
    def test_008(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        title_name = self.get_title()
        # 点击“首页活动”
        self.syhd()
        # 点击返回键
        self.fanhui()
        # 获取标题，判断是否返回到首页。
        self.assertEqual(self.get_title(), title_name, '功能异常')

    # 首页-》最新资讯，遍历“政策动态”、“沙包新闻”、“行业资讯”、“全部”。
    # @unittest.skip('暂不执行用例')
    def test_009(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“最新资讯”。
        self.zxzx()
        title_name = self.get_title()
        # 判断标题。
        self.assertEqual(title_name, "最新资讯", '功能异常')

        # 点击“政策动态”。
        self.zcdt()
        # 等待列表第一条记录加载完成。
        WebDriverWait(driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/index_information_content_layout")))
        # 获取并点击列表中的第一条记录标题。
        driver.find_element_by_id("com.seebon.shabaomanager:id/index_information_content_summary_tv").click()
        # 点击返回键
        self.fanhui()
        # 判断标题
        self.assertEqual(self.get_title(), title_name, '功能异常')

        # 点击“沙包新闻”。
        self.sbxw()
        # 等待列表加载完成。
        WebDriverWait(driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/index_information_content_layout")))
        # 点击列表中的第一条记录。
        driver.find_element_by_id("com.seebon.shabaomanager:id/index_information_content_layout").click()
        # 点击返回键
        self.fanhui()
        # 判断标题
        self.assertEqual(self.get_title(), title_name, '功能异常')

        # 点击“行业资讯”。
        self.hyzx()
        # 等待列表加载完成。
        WebDriverWait(driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/index_information_content_layout")))
        # 点击列表中的第一条记录。
        driver.find_element_by_id("com.seebon.shabaomanager:id/index_information_content_layout").click()
        # 点击返回键
        self.fanhui()
        # 判断标题
        self.assertEqual(self.get_title(), title_name, '功能异常')

        # 点击“全部”。
        self.qb()
        # 等待列表加载完成。
        WebDriverWait(driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/index_information_content_layout")))
        # 点击列表中的第一条记录。
        driver.find_element_by_id("com.seebon.shabaomanager:id/index_information_content_layout").click()
        # 点击返回键
        self.fanhui()
        # 判断标题
        self.assertEqual(self.get_title(), title_name, '功能异常')

        # 点击返回键，返回到首页。
        self.fanhui_zixun()
        # 获取标题，判断是否返回到首页。
        self.assertEqual(self.get_title(), "首页", '功能异常')

    # 首页-》商保理赔：跳转到对应功能页面。
    # @unittest.skip('暂不执行用例')
    def test_010(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“商保理赔”。
        self.sblp()
        # 判断标题
        title_name = driver.find_element_by_accessibility_id("商保理赔").get_attribute("name")
        self.assertEqual(title_name, "商保理赔", '功能异常')

    # 首页-》社保查询：跳转到对应功能页面。
    # @unittest.skip('暂不执行用例')
    def test_011(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“社保查询”。
        self.sbcx()
        # 等待“查询”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "查询")))
        # 判断标题
        title_name = driver.find_element_by_accessibility_id("社保查询").get_attribute("name")
        self.assertEqual(title_name, "社保查询", '功能异常')

    # 首页-》公积金查询：跳转到对应功能页面。
    # @unittest.skip('暂不执行用例')
    def test_012(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“公积金查询”。
        self.gjjcx()
        # 等待“查询”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "查询")))
        # 判断标题
        title_name = driver.find_element_by_accessibility_id("公积金查询").get_attribute("name")
        self.assertEqual(title_name, "公积金查询", '功能异常')

    # 首页-》个税计算器：跳转到对应功能页面。
    # @unittest.skip('暂不执行用例')
    def test_013(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“个税计算器”。
        self.gsjsq()
        # 等待“重置”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "重置")))
        # 判断标题
        title_name = driver.find_element_by_accessibility_id("个税计算器").get_attribute("name")
        self.assertEqual(title_name, "个税计算器", '功能异常')

    # 首页-》社保计算器：跳转到对应功能页面。
    # @unittest.skip('暂不执行用例')
    def test_014(self):
        driver = self.driver
        # 点击“首页”。
        self.shouye()
        # 点击“社保计算器”。
        self.sbjsq()
        # 等待“重置”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "重置")))
        # 判断标题
        title_name = driver.find_element_by_accessibility_id("社保计算器").get_attribute("name")
        self.assertEqual(title_name, "社保计算器", '功能异常')


if __name__ == '__main__':
    unittest.main()
    print("bye")







