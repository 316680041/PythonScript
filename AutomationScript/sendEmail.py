#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 
 
class sendEmail:
	def __init__(self,xlsFile,emailAddress):
		# SMTP 服务器
		self.mail_host    = '********'  			#设置服务器
		self.mail_user    = '********' 				#用户名
		self.mail_pass    = '********'   		   	#口令
		self.sender       = '********' 				#发送邮件
		self.receivers    = [emailAddress]  		#接收邮件
		self.xlsFile 	  = xlsFile
	def start(self):        
		Message = MIMEMultipart('related')
		Message['Subject'] = 'Zabbix报警提示表'
		att = MIMEText(open(self.xlsFile, 'rb').read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		att["Content-Disposition"] = 'attachment; filename="zabbix.xls"'
		Message.attach(att) 
		try:
		    smtp = smtplib.SMTP() 
		    smtp.connect(self.mail_host)
		    smtp.login(self.mail_user,self.mail_pass)  
		    smtp.sendmail(self.sender, self.receivers, Message.as_string())
		    smtp.quit()
		    print "send e-mail success"
		except smtplib.SMTPException:
		    print "send e-mail fail"