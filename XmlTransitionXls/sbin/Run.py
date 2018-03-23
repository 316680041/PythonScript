#!/usr/bin/python2.7
# coding=UTF-8 

'''该模块将xml里面的数据提取出来,转换到xls文件'''

__author__ = "jiegl"

import sys
import os
import optparse
sys.path.append("../libs")
from parseXml import parseXml
from transXlsx import transXlsx


''' 获取指定目录下的所有指定后缀的文件名 '''
def getFileName(path):
	data = []
	fileList = os.listdir(path)
	for i in fileList:
		# os.path.splitext():分离文件名与扩展名
		if os.path.splitext(i)[1] == '.xml':
			data.append(i)
	return data


'''主函数'''
def main():
	
	parser = optparse.OptionParser('usage %prog -s <save xlsx file directory>')    
	parser.add_option('-s', dest='saveFile', type='string', help='specify save xlsx file directory')
	(options, args) = parser.parse_args()    
	saveFile 	 = options.saveFile
	if saveFile == None:        
		print(parser.usage)        
		exit(0)
	else:
		#设置初始属性
		fileList  = getFileName("../data/bios/")
		dataList  = ['bios', 'memory', 'cpu', 'os']

		#实例化一个parseXml类的对象
		extractObject = parseXml()

		dataXml = []

		#遍历文件个数的次数
		for fileValue in fileList:
			#遍历查看数据信息个数的次数
			tmp = {}
			for dataValue in dataList:
				extractObject.setPath("../data/"+dataValue+"/"+fileValue+"")#设置xml文件路径
				if dataValue == 'bios':
					tmp["PSComputerName"] = extractObject.extract("S","N","__SERVER")
					tmp["SerialNumber"]   = extractObject.extract("S","N","SerialNumber")
					tmp["Manufacturer"]   = extractObject.extract("S","N","Manufacturer")
				elif dataValue == 'os':
					tmp["Caption"] = extractObject.extract("S","N","Caption")
				elif dataValue == 'cpu':
					tmp["CpuName"]  = extractObject.extract("S","N","Name")
					tmp["CpuCount"] = extractObject.extractCount("S","N","DeviceID")
				elif dataValue == 'memory':
					tmp["EndingAddress"] = round(float(extractObject.extract("U64","N","EndingAddress"))/1024/1024)
					tmp["EndingAddress"] = str(tmp["EndingAddress"]) + "G"
			dataXml.append(tmp)
		transXlsxObject = transXlsx()
		transXlsxObject.setSaveFile(saveFile)
		transXlsxObject.start(dataXml)

if __name__ == '__main__':    
	main()