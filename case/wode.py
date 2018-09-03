# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""说明：“我的”模块测试用例。"""
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.public import ShaBao
from casedata.basicdata import data_login
from time import sleep

account = data_login["account"]
password = data_login["password"]
new_password = data_login["new_password"]


class WoDe(ShaBao):
    # 我的-》设置-》功能介绍：判断版本名称（版本号）是否正确。
    #@unittest.skip('暂不执行用例')
    def test_001(self):
        version_name1 = "沙包 v1.1.0主要更新"
        driver = self.driver
        # 点击“我的”。
        self.wode()
        # 点击“设置”。
        self.sz()
        # 点击“功能介绍”。
        self.gnjs()
        # 判断标题。
        self.assertEqual(self.get_title(), "功能介绍", '功能异常')
        # 获取版本名称。
        version_name2 = driver.find_element_by_id("com.seebon.shabaomanager:id/app_function_version_tv").get_attribute("name")
        # 判断版本名称是否正确。
        self.assertEqual(version_name2, version_name1, msg='版本名称不正确')

    # 我的-》设置-》意见反馈：填写并提交反馈信息，不上传图片。
    #@unittest.skip('暂不执行用例')
    def test_002(self):
        feedback_info = "反馈信息测试"
        driver = self.driver
        # 点击“我的”。
        self.wode()
        # 点击“设置”。
        self.sz()
        # 点击“意见反馈”。
        self.yjfk()
        # 判断标题。
        self.assertEqual(self.get_title(), "填写反馈内容", '功能异常')
        # 选择反馈类型。
        # 选择“社保业务”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/checkbox_shebao").click()
        # 选择“公积金业务”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/checkbox_gjj").click()
        # 选择“工资业务”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/checkbox_salary").click()
        # 选择“账号相关”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/checkbox_number").click()
        # 选择“APP不稳定”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/checkbox_not_stable").click()
        # 选择“提供建议”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/checkbox_suggest").click()
        # 选择“其他问题”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/checkbox_other").click()
        # 填写反馈内容。
        driver.find_element_by_id("com.seebon.shabaomanager:id/feedback_input_et").send_keys(feedback_info)
        # 点击“添加图片”。
        self.tjtp()
        # 点击“取消”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/take_photo_from_cancel").click()
        # 判断标题。
        self.assertEqual(self.get_title(), "填写反馈内容", '功能异常')
        # 点击“添加图片”。
        self.tjtp()
        # 点击“从手机相册选择”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/take_photo_from_gallery").click()
        driver.press_keycode(4)
        # 判断标题。
        self.assertEqual(self.get_title(), "填写反馈内容", '功能异常')
        # 点击“添加图片”。
        self.tjtp()
        # 点击“拍照”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/take_photo_from_capture").click()
        sleep(3)
        driver.press_keycode(4)
        # 判断标题。
        self.assertEqual(self.get_title(), "填写反馈内容", '功能异常')
        # 点击“提交”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/toolbar_commit").click()
        # 判断标题。
        self.assertEqual(self.get_title(), "设置", '功能异常')

    # 我的-》设置-》关于我们：查看页面标题是否正确。
    #@unittest.skip('暂不执行用例')
    def test_003(self):
        driver = self.driver
        # 点击“我的”。
        self.wode()
        # 点击“设置”。
        self.sz()
        # 点击“关于我们”。
        self.gywm()
        # 判断标题。
        self.assertEqual(self.get_title(), "关于我们", '功能异常')

    # 我的-》设置-》清除缓存，清除缓存功能。
    #@unittest.skip('暂不执行用例')
    def test_004(self):
        driver = self.driver
        # 点击“我的”。
        self.wode()
        # 点击“设置”。
        self.sz()
        # 获取缓存数值。
        cache_size1 = driver.find_element_by_id("com.seebon.shabaomanager:id/account_setting_cache_size_tv").get_attribute("name")
        print(cache_size1)
        # 点击“清除缓存”。
        self.qchc()
        # 获取页面信息。
        alert_name1 = driver.find_element_by_id("com.seebon.shabaomanager:id/alertTitle").get_attribute("name")
        alert_name2 = driver.find_element_by_id("com.seebon.shabaomanager:id/message").get_attribute("name")
        alert_name3 = driver.find_element_by_id("com.seebon.shabaomanager:id/button1").get_attribute("name")
        alert_name4 = driver.find_element_by_id("com.seebon.shabaomanager:id/button2").get_attribute("name")
        # 判断提示标题。
        self.assertEqual(alert_name1, "温馨提示", '功能异常')
        # 判断提示内容。
        self.assertEqual(alert_name2, "是否清除缓存", '功能异常')
        # 判断确定按钮。
        self.assertEqual(alert_name3, "确定", '功能异常')
        # 判断取消按钮。
        self.assertEqual(alert_name4, "取消", '功能异常')
        # 在弹出的温馨提示页面，点击“取消”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/button2").click()
        # 获取缓存数值。
        cache_size2 = driver.find_element_by_id("com.seebon.shabaomanager:id/account_setting_cache_size_tv").get_attribute("name")
        print(cache_size2)
        self.assertEqual(cache_size2, cache_size1, '功能异常')
        # 点击“清除缓存”。
        self.qchc()
        # 在弹出的温馨提示页面，点击“确定”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/button1").click()
        # 获取缓存数值。
        cache_size3 = driver.find_element_by_id("com.seebon.shabaomanager:id/account_setting_cache_size_tv").get_attribute("name")
        print(cache_size3)
        self.assertEqual(cache_size3, '无', '功能异常')

    # 我的-》设置-》新消息提醒：跳转到新消息提醒页面。
    #@unittest.skip('暂不执行用例')
    def test_005(self):
        driver = self.driver
        # 点击“我的”。
        self.wode()
        # 点击“设置”。
        self.sz()
        # 点击“新消息提醒”
        self.xxxtx()
        # 判断标题。
        self.assertEqual(self.get_title(), "新消息提醒", '功能异常')

    # 我的-》设置-》安全中心-》修改登录密码：修改登录密码功能。
    #@unittest.skip('暂不执行用例')
    def test_006(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“我的”。
        self.wode()
        # 点击“设置”。
        self.sz()
        # 点击“安全中心”。
        self.aqzx()
        # 点击“修改登录密码”。
        self.xgdlmm()
        # 判断标题。
        self.assertEqual(self.get_title(), "修改登录密码", '功能异常')
        # 输入原密码、新密码。
        driver.find_element_by_id("com.seebon.shabaomanager:id/account_old_login_psw_edittext").send_keys(password)
        driver.find_element_by_id("com.seebon.shabaomanager:id/account_new_login_psw_edittext").send_keys(new_password)
        # 点击“保存新密码”。
        self.bcxmm()
        # 判断标题。
        self.assertEqual(self.get_title(), "安全中心", '功能异常')
        print("修改新密码成功")
        # 点击“修改登录密码”。
        self.xgdlmm()
        # 输入新密码、原密码，改回原密码。
        driver.find_element_by_id("com.seebon.shabaomanager:id/account_old_login_psw_edittext").send_keys(new_password)
        driver.find_element_by_id("com.seebon.shabaomanager:id/account_new_login_psw_edittext").send_keys(password)
        # 点击“保存新密码”。
        self.bcxmm()
        # 判断标题。
        self.assertEqual(self.get_title(), "安全中心", '功能异常')
        print("改回原密码成功")

    # 我的-》鼓励下我们：跳转到对应的应用市场。
    #@unittest.skip('暂不执行用例')
    def test_007(self):
        driver = self.driver
        # 点击“我的”。
        self.wode()
        # 点击“鼓励下我们”
        self.glxwm()
        # 点击返回键
        driver.press_keycode(4)
        # 判断标题。
        self.assertEqual(self.get_title(), "我的", '功能异常')

    # 我的-》推荐给朋友：查看分享平台。
    #@unittest.skip('暂不执行用例')
    def test_008(self):
        driver = self.driver
        # 点击“我的”。
        self.wode()
        # 点击“推荐给我们”。
        self.tjgpy()
        # 点击分享平台
        #driver.find_element_by_id("com.seebon.shabaomanager:id/share_qq_imgview").click()
        #driver.find_element_by_id("com.seebon.shabaomanager:id/share_wechat_imgview").click()
        #driver.find_element_by_id("com.seebon.shabaomanager:id/share_sina_weibo_imgview").click()
        # 点击取消按钮
        driver.find_element_by_id("com.seebon.shabaomanager:id/share_cancel_img").click()
        # 判断标题。
        self.assertEqual(self.get_title(), "我的", '功能异常')

    # 我的-》联系客服：发送消息功能。
    #@unittest.skip('暂不执行用例')
    def test_009(self):
        send_message = "发送消息功能测试"
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“我的”。
        self.wode()
        # 点击“联系客服”。
        self.lxkf()
        # 判断标题。
        self.assertEqual(self.get_title(), "沙小包", '功能异常')
        # 点击信息编辑框，输入需发送的消息。
        driver.find_element_by_id("com.seebon.shabaomanager:id/send_content_edit").click()
        driver.find_element_by_id("com.seebon.shabaomanager:id/send_content_edit").send_keys(send_message)
        # 点击“发送”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/btn_text_send").click()
        # 判断发送的消息。
        message = driver.find_element_by_name(send_message).get_attribute("name")
        self.assertEqual(message, send_message, '功能异常')

    # 我的-》联系客服-》电话联系：跳转到拨号页面。
    #@unittest.skip('暂不执行用例')
    def test_010(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“我的”。
        self.wode()
        # 点击“联系客服”。
        self.lxkf()
        # 判断标题。
        self.assertEqual(self.get_title(), "沙小包", '功能异常')
        # 点击“电话联系”。
        self.dhlx()
        # 判断联系电话。
        phone_number = driver.find_element_by_id("com.android.contacts:id/digits").get_attribute("name")
        self.assertEqual(phone_number, "4008358155", '功能异常')
        # 点击“返回键”。
        driver.press_keycode(4)
        # 判断标题。
        self.assertEqual(self.get_title(), "沙小包", '功能异常')

    # 我的-》联系客服-》微信公众号：添加微信公众号提示页面展示。
    #@unittest.skip('暂不执行用例')
    def test_011(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“我的”。
        self.wode()
        # 点击“联系客服”。
        self.lxkf()
        # 判断标题。
        self.assertEqual(self.get_title(), "沙小包", '功能异常')
        # 点击“微信公众号”。
        self.wxgzh()
        # 判断提示标题。
        content = driver.find_element_by_id("com.seebon.shabaomanager:id/alertTitle").get_attribute("name")
        self.assertEqual(content, "添加公众号了解更多", '功能异常')
        # 判断提示内容。
        content = driver.find_element_by_id("com.seebon.shabaomanager:id/message").get_attribute("name")
        self.assertEqual(content, "已为您复制公众号：shabaozaixian，打开微信关注公众号？", '功能异常')
        # 判断“打开”按钮。
        content = driver.find_element_by_id("com.seebon.shabaomanager:id/button1").get_attribute("name")
        self.assertEqual(content, "打开", '功能异常')
        # 判断“取消”按钮。
        content = driver.find_element_by_id("com.seebon.shabaomanager:id/button2").get_attribute("name")
        self.assertEqual(content, "取消", '功能异常')

    # 我的-》联系客服-》微信公众号：在添加微信公众号页面，点击“取消”、“打开”。
    #@unittest.skip('暂不执行用例')
    def test_012(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“我的”。
        self.wode()
        # 点击“联系客服”。
        self.lxkf()
        # 判断标题。
        self.assertEqual(self.get_title(), "沙小包", '功能异常')
        # 点击“微信公众号”。
        self.wxgzh()
        # 点击“取消”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/button2").click()
        # 判断标题。
        self.assertEqual(self.get_title(), "沙小包", '功能异常')
        # 点击“微信公众号”。
        self.wxgzh()
        # 点击“打开”。
        driver.find_element_by_id("com.seebon.shabaomanager:id/button1").click()
        # 点击返回键。
        driver.press_keycode(4)
        # 判断标题。
        content = self.get_title()
        self.assertEqual(content, "沙小包", '功能异常')

    # 我的-》我的签署，遍历我的签署子页面。
    #@unittest.skip('暂不执行用例')
    def test_013(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“我的”。
        self.wode()
        # 点击“我的签署”。
        self.wdqs()
        # 点击“待我签署”。
        self.dwqs()
        # 判断标题。
        self.assertEqual(self.get_title(), '待我签署', msg='功能异常')
        self.fanhui()
        # 点击“待他人签署”。
        self.dtrqs()
        # 判断标题。
        self.assertEqual(self.get_title(), '待他人签署', msg='功能异常')
        self.fanhui()
        # 点击“已完成签署”。
        self.ywcqs()
        # 判断标题。
        self.assertEqual(self.get_title(), '已完成签署', msg='功能异常')
        self.fanhui()
        # 判断标题。
        self.assertEqual(self.get_title(), '我的签署', msg='功能异常')

    # 我的-》我的参保人：跳转到参保人页面。
    #@unittest.skip('暂不执行用例')
    def test_014(self):
        driver = self.driver
        self.logout()
        self.grxx()
        self.login(account, password)
        # 点击“我的”。
        self.wode()
        # 点击“我的参保人”。
        self.wdcbr()
        # 判断标题。
        self.assertEqual(self.get_title(), '参保人', msg='功能异常')
        # 点击“查看更多信息”。
        self.ckgdxx()
        # 判断标题。
        sleep(3)
        self.assertEqual(self.get_title(), '个人信息', msg='功能异常')

    # 我的-》个人信息：登录操作。
    #@unittest.skip('暂不执行用例')
    def test_015(self):
        driver = self.driver
        self.logout()
        # 点击“个人信息”。
        self.grxx()
        self.login(account, password)
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ID, "com.seebon.shabaomanager:id/mine_account_name")))
        company_name = driver.find_element_by_id("com.seebon.shabaomanager:id/mine_account_belongto_company").get_attribute("name")
        self.assertNotEqual(company_name, "点击登录", msg='功能异常')

    # 我的-》个人信息-》注册账号：正常跳转到注册页面。
    #@unittest.skip('暂不执行用例')
    def test_016(self):
        driver = self.driver
        self.logout()
        # 点击“个人信息”。
        self.grxx()
        # 点击“注册账号”。
        self.zczh()
        # 判断标题。
        self.assertEqual(self.get_title(), "注册", '功能异常')
        # 点击返回键。
        driver.press_keycode(4)
        # 判断标题。
        self.assertEqual(self.get_title(), "登录", '功能异常')

    # 我的-》个人信息-》注册账号-》《沙包管家服务协议》：正常跳转到协议页面。
    #@unittest.skip('暂不执行用例')
    def test_017(self):
        driver = self.driver
        self.logout()
        # 点击“个人信息”。
        self.grxx()
        # 点击“注册账号”，并判断是否跳转到注册页面。
        self.zczh()
        # 点击“《沙包管家服务协议》”。
        self.sbgjfwxy()
        # 判断标题。
        self.assertEqual(self.get_title(), "用户注册及使用APP隐私协议", '功能异常')
        # 点击返回键。
        driver.press_keycode(4)
        # 判断标题。
        self.assertEqual(self.get_title(), "注册", '功能异常')

    # 我的-》个人信息-》忘记密码：正常跳转到重置密码页面。
    #@unittest.skip('暂不执行用例')
    def test_018(self):
        driver = self.driver
        self.logout()
        # 点击“个人信息”。
        self.grxx()
        # 点击“忘记密码？”
        self.wjmm()
        # 判断标题。
        self.assertEqual(self.get_title(), "重置密码", '功能异常')
        # 点击返回键
        driver.press_keycode(4)
        # 判断标题。
        self.assertEqual(self.get_title(), "登录", '功能异常')


if __name__ == '__main__':
    unittest.main()
    print("bye")
