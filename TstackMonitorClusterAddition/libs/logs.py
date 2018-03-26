#!/usr/bin/python2.7
# coding=UTF-8 

import sys

class logs: 

	#构造函数不处理任何操作
	def __init__(self):
		pass

	def Start(self,filename):    
		self.output = sys.stdout
		self.outputfile  = open(filename,'a+')
		sys.stdout  = self.outputfile
		
	def Close(self,):    
		try:        
			self.outputfile.close()
			sys.stdout = self.output
		except:        
			print('[-] Error No Connect File')        
			exit(0)