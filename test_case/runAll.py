#coding:utf-8
#@Time    : 2018/11/21 14:05
#@Author  : 
#@File    : runAll.py
import os
import time
import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport


#用例路径
case_path = os.path.join(os.getcwd())

#报告存放路径
report_path = '..\\create_report\\'
#report_path = os.path.join(os.getcwd(), 'report')

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    # 2、html报告文件路径
    report_abspath = os.path.join(report_path,now + ".html")
    # 3、打开一个文件，将result写入此file中
    #fp = open(report_abspath, "wb")
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'放假通知',description=u'详细信息如下')
    # 4、调用add_case函数返回值
    # runner.run(all_case())
    runner = BeautifulReport(all_case()).report(filename=now, description='放假通知',
                                        log_path=report_path)  # log_path='.'把report放到当前目录下




    #fp.close()


