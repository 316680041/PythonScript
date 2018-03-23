#!/usr/bin/python2.7
# coding=UTF-8 

'''该模块可以将csv文档转成UTF-8编码的xls文档,并发送到指定邮箱'''

__author__ = "jiegl"

import optparse
from transCoding import transCoding
from sendEmail import sendEmail

def main():
	parser = optparse.OptionParser('usage %prog -f <csv file name> -s <save xlsx file directory> -e <send e-mail address>')    
	parser.add_option('-f', dest='fileName', type='string', help='specify csv file name')
	parser.add_option('-s', dest='saveFile', type='string', help='specify save xlsx file directory')
	parser.add_option('-e', dest='emailAddress', type='string', help='specify send e-mail address')
	(options, args) = parser.parse_args()    
	fileName 	 = options.fileName
	saveFile 	 = options.saveFile
	emailAddress = options.emailAddress
	if fileName == None or saveFile == None or emailAddress == None:        
		print(parser.usage)        
		exit(0)
	else:        
		transCodingObject = transCoding(fileName,saveFile)
		transCodingObject.start()
		sendEmailObject = sendEmail(saveFile,emailAddress)
		sendEmailObject.start()

if __name__ == '__main__':    
	main()