#!/usr/bin/python2.7
# coding=UTF-8 

from pexpect import pxssh

class Remote: 

	#构造函数不处理任何操作
	def __init__(self):
		pass

	def SendCommand(self,cmd):    
		self.child.sendline(cmd)    
		self.child.prompt()    
		print(self.child.before)
		
	def Connect(self,host, user, password):    
		try:        
			s = pxssh.pxssh()        
			s.login(host, user, password)
			self.child = s
		except:        
			print('[-] Error Connecting')        
			exit(0)