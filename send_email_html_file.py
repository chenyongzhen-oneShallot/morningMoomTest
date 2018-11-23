#coding:utf-8
#@Time    : 2018/11/21 14:42
#@Author  : 陈勇臻
#@File    : send_email_html_file.py

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import unittest
import time
import os


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((\
        Header(name, 'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))


## ==============定义发送附件邮件==========
def send_file(file_new,file_attach):
    smtpserver = 'smtp.qq.com'
    user = '891354032@qq.com'
    password = ''
    sender = '891354032@qq.com'
    receiver = 'cyz891354032@163.com'

    file = open(file_new, 'r',encoding='utf-8').read()
    file1 = open(file_attach, 'r', encoding='utf-8').read()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    subject = '放假通知' + now

    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = '迷途小书童_臻<891354032@qq.com>'
    msg_to = ['<cyz891354032@163.com>', '<891354032@qq.com>']
    #msg['To'] = "<cyz891354032@163.com>"
    msg['To'] = ','.join(msg_to)

    #att=MIMEText(sendfile,"base64","utf-8")

    # msg_html1 = MIMEText(file, 'html', 'utf-8')
    # msg.attach(msg_html1)


    msg_html = MIMEText(file, 'html', 'utf-8')
    #msg_html["Content-Disposition"] = 'attachment; filename="chenyz.html"'
    msg.attach(msg_html)

    msg_html1 = MIMEText(file1, 'html', 'utf-8')
    msg_html1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html1)




    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver,msg.as_string())
    smtp.quit()


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序 win
    #lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # linux
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    return file_new
