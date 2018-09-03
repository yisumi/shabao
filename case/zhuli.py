# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""说明：“助理”模块测试用例。"""
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.public import gesjs_biaozhun
from public.public import ShaBao
from casedata.basicdata import data_gsjsq
from casedata.basicdata import data_login

account = data_login["account"]
password = data_login["password"]

class ZhuLi(ShaBao):
    # 助理-》在线客服：发送消息功能。
    #@unittest.skip('暂不执行用例')
    def test_001(self):
        send_message = "发送消息功能测试"
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“助理”。
        self.zhuli()
        # 点击“在线客服”。
        self.zxkf()
        # 点击信息编辑框，输入需发送的消息。
        driver.find_element_by_id("com.seebon.shabaomanager:id/send_content_edit").click()
        driver.find_element_by_id("com.seebon.shabaomanager:id/send_content_edit").send_keys(send_message)
        # 点击“发送”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/btn_text_send").click()
        # 判断发送的消息。
        message = driver.find_element_by_name(send_message).get_attribute("name")
        self.assertEqual(message, send_message, '功能异常')

    # 助理-》常见问题：信息展示功能。
    #@unittest.skip('暂不执行用例')
    def test_002(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“常见问题”。
        self.cjwt()
        content1 = self.get_title()
        # 等待第一条记录加载完成，并点击。
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/helper_title_tv")))
        driver.find_element_by_id("com.seebon.shabaomanager:id/helper_title_tv").click()
        # 点击返回键。
        self.fanhui()
        content2 = self.get_title()
        # 判断标题。
        self.assertEqual(content2, content1, '功能异常')

    # 助理-》使用手册：信息展示功能。
    #@unittest.skip('暂不执行用例')
    def test_003(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“使用手册”。
        self.sysc()
        content1 = self.get_title()
        # 等待第一条记录加载完成，并点击。
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/helper_title_tv")))
        driver.find_element_by_id("com.seebon.shabaomanager:id/helper_title_tv").click()
        # 点击返回键。
        self.fanhui()
        content2 = self.get_title()
        # 判断标题。
        self.assertEqual(content2, content1, '功能异常')

    # 助理-》政策查询：信息展示功能。
    #@unittest.skip('暂不执行用例')
    def test_004(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“政策查询”。
        self.zccx()
        content1 = self.get_title()
        # 等待第一条记录加载完成，并点击。
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/helper_title_tv")))
        driver.find_element_by_id("com.seebon.shabaomanager:id/helper_title_tv").click()
        # 点击返回键。
        self.fanhui()
        content2 = self.get_title()
        # 判断标题。
        self.assertEqual(content2, content1, '功能异常')

    # 助理-》个税计算器：计算功能。
    #@unittest.skip('暂不执行用例')
    def test_005(self):
        gsdata = data_gsjsq
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“个税计算器”。
        self.gsjsq()
        # 等待“重置”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "重置")))
        # 判断标题
        content = driver.find_element_by_accessibility_id("个税计算器").get_attribute("name")
        self.assertEqual(content, "个税计算器", '功能异常')
        print("一共有%d组测试数据" % len(gsdata))
        fault_num = 0
        for i in range(len(gsdata)):
            result = self.gsjs(gsdata[i][0], gsdata[i][1], gsdata[i][2], gsdata[i][3])
            biaozhun = gesjs_biaozhun(gsdata[i][0], gsdata[i][1], gsdata[i][2], gsdata[i][3])
            if result == biaozhun:
                print("第%d组结果一致！" % (i+1))
            else:
                fault_num = fault_num + 1
                print("第%d组结果不一致，数据组为：" % (i + 1), end="")
                print(gsdata[i])
                print("计算结果为：", end="")
                print(result)
                print("标准结果为：", end="")
                print(biaozhun)
        print('出错数据共%d组' % fault_num)
        self.assertEqual(fault_num, 0, '功能异常')

    # 助理-》个税计算器：重置功能提示页面展示。
    #@unittest.skip('暂不执行用例')
    def test_006(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“个税计算器”。
        self.gsjsq()
        # 等待“重置”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "重置")))
        # 点击“重置”。
        self.driver.find_element_by_accessibility_id("重置").click()
        # 判断提示页面。
        content1 = self.driver.find_element_by_accessibility_id("").get_attribute("name")
        content2 = self.driver.find_element_by_accessibility_id("").get_attribute("name")
        content3 = self.driver.find_element_by_accessibility_id("").get_attribute("name")
        self.assertEqual(content1, "确定重置所有输入选项吗？", '功能异常')
        self.assertEqual(content2, "取消", '功能异常')
        self.assertEqual(content3, "确定", '功能异常')

    # 助理-》个税计算器：重置功能提示页面，点击“取消”。
    #@unittest.skip('暂不执行用例')
    def test_007(self):
        gsdata = data_gsjsq
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“个税计算器”。
        self.gsjsq()
        # 等待“重置”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "重置")))
        # 输入/选择值。
        self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.EditText').send_keys(str(gsdata[0][0]))
        self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.EditText').send_keys(str(gsdata[0][1]))
        self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.EditText').send_keys(str(gsdata[0][2]))
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="3500"]').click()
        # 获取输入框内的值。
        shuiqian1 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.EditText').get_attribute("name")
        shebao1 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.EditText').get_attribute("name")
        gongjijin1 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.EditText').get_attribute("name")
        qizhengdian1 = self.driver.find_element_by_xpath('//android.view.View[@content-desc="4800"]').get_attribute("name")
        # 点击“重置”。
        self.driver.find_element_by_accessibility_id("重置").click()
        # 点击“取消”
        self.driver.find_element_by_accessibility_id("取消").click()
        # 再次获取输入框内的值。
        shuiqian2 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.EditText').get_attribute("name")
        shebao2 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.EditText').get_attribute("name")
        gongjijin2 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.EditText').get_attribute("name")
        qizhengdian2 = self.driver.find_element_by_xpath('//android.view.View[@content-desc="4800"]').get_attribute("name")
        self.assertEqual(shuiqian2, shuiqian1, '功能异常')
        self.assertEqual(shebao2, shebao1, '功能异常')
        self.assertEqual(gongjijin2, gongjijin1, '功能异常')
        self.assertEqual(qizhengdian2, qizhengdian1, '功能异常')

    # 助理-》个税计算器：重置功能提示页面，点击“确定”。
    #@unittest.skip('暂不执行用例')
    def test_008(self):
        gsdata = data_gsjsq
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“个税计算器”。
        self.gsjsq()
        # 等待“重置”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "重置")))
        # 获取输入框内的值。
        shuiqian1 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.EditText').get_attribute("name")
        shebao1 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.EditText').get_attribute("name")
        gongjijin1 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.EditText').get_attribute("name")
        qizhengdian1 = self.driver.find_element_by_xpath('//android.view.View[@content-desc="3500"]').get_attribute("name")
        # 输入/选择值。
        self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.EditText').send_keys(str(gsdata[0][0]))
        self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.EditText').send_keys(str(gsdata[0][1]))
        self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.EditText').send_keys(str(gsdata[0][2]))
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="3500"]').click()
        # 点击“重置”。
        self.driver.find_element_by_accessibility_id("重置").click()
        # 点击“确定”
        self.driver.find_element_by_accessibility_id("确定").click()
        # 再次获取输入框内的值。
        shuiqian2 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.EditText').get_attribute("name")
        shebao2 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.EditText').get_attribute("name")
        gongjijin2 = self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.EditText').get_attribute("name")
        qizhengdian2 = self.driver.find_element_by_xpath('//android.view.View[@content-desc="3500"]').get_attribute("name")
        self.assertEqual(shuiqian2, shuiqian1, '功能异常')
        self.assertEqual(shebao2, shebao1, '功能异常')
        self.assertEqual(gongjijin2, gongjijin1, '功能异常')
        self.assertEqual(qizhengdian2, qizhengdian1, '功能异常')

    # 助理-》社保计算器：跳转到对应功能页面。
    #@unittest.skip('暂不执行用例')
    def test_009(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“社保计算器”。
        self.sbjsq()
        # 等待“重置”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "重置")))
        # 判断标题
        content = driver.find_element_by_accessibility_id("社保计算器").get_attribute("name")
        self.assertEqual(content, "社保计算器", '功能异常')

    # 助理-》商保理赔：跳转到对应功能页面。
    #@unittest.skip('暂不执行用例')
    def test_010(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“商保理赔”。
        self.sblp()
        # 判断标题
        content = driver.find_element_by_accessibility_id("商保理赔").get_attribute("name")
        self.assertEqual(content, "商保理赔", '功能异常')

    # 助理-》社保查询：跳转到对应功能页面。
    #@unittest.skip('暂不执行用例')
    def test_011(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“社保查询”。
        self.sbcx()
        # 等待“查询”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "查询")))
        # 判断标题
        content = driver.find_element_by_accessibility_id("社保查询").get_attribute("name")
        self.assertEqual(content, "社保查询", '功能异常')

    # 助理-》公积金查询：跳转到对应功能页面。
    #@unittest.skip('暂不执行用例')
    def test_012(self):
        driver = self.driver
        # 点击“助理”。
        self.zhuli()
        # 点击“公积金查询”。
        self.gjjcx()
        # 等待“查询”按钮加载完成。
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.NAME, "查询")))
        # 判断标题
        content = driver.find_element_by_accessibility_id("公积金查询").get_attribute("name")
        self.assertEqual(content, "公积金查询", '功能异常')


if __name__ == '__main__':
    unittest.main()
    print("bye")







