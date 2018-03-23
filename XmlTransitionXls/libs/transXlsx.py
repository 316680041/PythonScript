#!/usr/bin/python2.7
# coding=UTF-8 

'''该模块负责将数据写入xls文件里面'''

__author__ = "jiegl"

import xlwt

class transXlsx:
	def __init__(self):
		pass

	def setSaveFile(self,saveFile):
		self.saveFile = saveFile

	def start(self,dataXml):
		myexcel  = xlwt.Workbook(encoding='utf-8')
		mysheet  = myexcel.add_sheet("Server")
		mysheet.write(0,0,"服务器主机名")
		mysheet.write(0,1,"S/N")
		mysheet.write(0,2,"硬件供应商")
		mysheet.write(0,3,"OS名称、版本")
		mysheet.write(0,4,"CPU")
		mysheet.write(0,5,"CPU个数")
		mysheet.write(0,6,"内存")
		i = 1
		for dataXmlValue in dataXml:
			mysheet.write(i,0,dataXmlValue["PSComputerName"])
			mysheet.write(i,1,dataXmlValue["SerialNumber"])
			mysheet.write(i,2,dataXmlValue["Manufacturer"])
			mysheet.write(i,3,dataXmlValue["Caption"])
			mysheet.write(i,4,dataXmlValue["CpuName"])
			mysheet.write(i,5,dataXmlValue["CpuCount"])
			mysheet.write(i,6,dataXmlValue["EndingAddress"])
			i += 1
		myexcel.save(self.saveFile)