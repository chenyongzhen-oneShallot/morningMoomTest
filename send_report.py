#coding:utf-8
#@Time    : 2018/11/21 14:40
#@Author  : 陈勇臻
#@File    : send_report.py
import time
import unittest
import os
import HTMLTestRunner
import send_email_html_file
from BeautifulReport import BeautifulReport
import shutil
#from test_case.runAll import all_case


# 用例目录
test_suite_dir = r'test_case\\'
# test_suite_dir=r'/opt/openapi/'  #145部署环境
# 报告目录
Report_dir = r'send_report\\'


# Report_dir=r'/opt/openapi/Report/'  #145部署环境
def creatsuite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = test_suite_dir
    # 定义 discover 方法的参数
    package_tests = unittest.defaultTestLoader.discover(test_dir,
                                                        pattern='test*.py',
                                                        top_level_dir=None)
    # package_tests=TestLoader.discover(start_dir=test_dir, pattern='Test*.py')
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in package_tests:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


alltestnames = creatsuite()


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = Report_dir
    filename =test_report + now + '_email.html'
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'放假通知',
        description=u'放假通知'
    )
    #runner = BeautifulReport(all_case()).report(filename=now, description='放假通知',log_path=test_report)  # log_path='.'把report放到当前目录下

    runner.run(alltestnames)

    fp.close()
    #shutil.copy(filename, Report_dir)
    new_report = send_email_html_file.new_report(test_report)
    new_attach = send_email_html_file.new_report("create_report")

    # 发送测试报告
    send_email_html_file.send_file(new_report,new_attach)




