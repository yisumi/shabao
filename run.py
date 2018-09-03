# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""说明：执行测试用例。"""
import unittest
import HTMLTestRunner
import time
import os

"""

from case import test_shouye
from case import test_zhuli
from case import test_wode

# 构造测试集
suite = unittest.TestSuite()
suite.addTest(shouye.ShouYe('test_cs'))
suite.addTest(zhuli.ZhuLi('test_cjwt'))
suite.addTest(zhuli.ZhuLi('test_sysc'))

"""

# 获取所有用例，使用unittest.TestLoader中的discover方法，discover(start_dir, pattern='test*.py',top_level_dir=None)。
# case_dir:待执行用例的目录。
# pattern：匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。
# top_level_dir：顶层目录的名称，一般默认等于None即可。
# 方法作用：递归查找指定目录（start_dir）及其子目录下的全部测试模块，将这些测试模块放入一个TestSuite对象并返回。
# 如果一个测试文件的名称符合pattern，将检查该文件是否包含 load_tests() 函数，
# 如果 load_tests() 函数存在，则由该函数负责加载本文件中的测试用例。
# 如果不存在，则执行loadTestsFromModule()，查找该文件中派生自TestCase 的类包含的 test 开头的方法。


def all_case():
    # 获取test_case文件夹的的绝对路径。
    case_path = os.path.join(os.getcwd(), "case")
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    print(discover)
    return discover


if __name__ == '__main__':

    """
    
    # 不引入HTMLTestRunner，即只使用unittest时，执行测试用例。
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
    """

    from case import shouye

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(shouye.ShouYe('test_002'))

    # 获取当前时间，并将当前时间添加到测试报告名称中。
    nowtime = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
    # 定义报告的存放路径，支持绝对路径和相对路径。
    reportpath = "D:\\install\\py-projects\\shabao_project\\report\\自动化测试报告-沙包管家android-V1.2.6-%s.html" % nowtime
    reportname = '自动化测试报告-沙包管家android-V1.2.6-%s.html' % nowtime
    fp = open(reportpath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=reportname,
        description='appiumdesktop版本：1.6.5 ******* '
                    '测试设备：三星-Galaxy A3, SM-A3000, Android-5.0.2'

    )
    runner.run(suite)
    fp.close()


# ---------------------------------------------------------------------------------------------
    # 发送邮件
    from email.mime.text import MIMEText
    import smtplib

    # 发件人数据
    smtpserver = 'smtp.126.com'
    username = 'linh216@126.com'
    password = '126com,lh.'
    sender = 'linh216@126.com'

    # 收件人数据
    receiver = ['linh216@sina.com', '406607983@qq.com']

    # 一、构造邮件
    from email.mime.multipart import MIMEMultipart
    from email.mime.multipart import MIMEBase
    from email import encoders
    msg = MIMEMultipart()

    # 1、邮件正文
    msg.attach(MIMEText('%s已经生成，请查收！' % reportname, 'plain', 'utf-8'))
    # 2、邮件主题
    msg['subject'] = reportname
    # 3、发件人
    msg['from'] = 'tester<%s>' % sender
    # 4、收件人
    msg['to'] = 'Tom<%s>,Michael<%s>' % (receiver[0], receiver[1])

    # 5、添加附件
    with open('%s' % reportpath, 'rb') as f:
        # 设置邮件的MIME和文件名，'html'表示类型
        mime = MIMEBase('html', 'html', filename=reportname)

        # 添加必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename=reportname)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')

        # 把附件等内容读进来
        mime.set_payload(f.read())
        # 使用Base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart
        msg.attach(mime)

    # 二、发送邮件
    smtp = smtplib.SMTP(smtpserver, 25)
    # 也可使用以下两行代替：
    # smtp = smtplib.SMTP()
    # smtp.connect(smtpserver)

    # 打印与SMTP服务器交互的信息
    smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

















