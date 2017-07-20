#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : email_agent
# Fatures:
# Author : qianyong
# Time   : 2017-06-19 11:39
# Version: V0.0.1
#



from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

def send_qq_email(title,content):
    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    #sender_qq为发件人的qq号码
    sender_qq = '1060591592'
    #pwd为qq邮箱的授权码
    pwd = 'xiokxwcrwhbibddb'
    #发件人的邮箱
    sender_qq_mail = '1060591592@qq.com'
    #收件人邮箱
    receiver = ['1060591592@qq.com','375069290@qq.com']
    #邮件的正文内容
    mail_content = content
    #邮件标题
    mail_title = title
    try:
        #ssl登录
        smtp = SMTP_SSL(host_server)
        #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
        print('发送 邮件成功 ')
    except Exception as e:
        print('发送 邮件失败,原因是 {}'.format(e))
    #只需要更改host_server 、sender_qq、pwd、sender_qq_mail、receiver、mail_content、mail_title等数据，就可以实现简单的发送任务。
    #MIMEText函数中的第二个参数为“plain”时，发送的是text文本。如果为“html”，则能发送网页格式文本邮件。

if __name__ == '__main__':
    send_qq_email('风控日志1','测试')
