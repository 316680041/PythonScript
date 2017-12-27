#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# SMTP 服务器
mail_host = "smtp.163.com"  		#设置服务器
mail_user = '********'    #用户名
mail_pass = '********'   		    #口令

sender    = '********'    #发送邮件
receivers = ['********']  #接收邮件

msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header('python email test', 'utf-8')
 
 
try:
    smtp = smtplib.SMTP() 
    smtp.connect(mail_host)
    smtp.login(mail_user,mail_pass)  
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print "ok"
except smtplib.SMTPException:
    print "fail"