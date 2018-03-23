#!/usr/bin/python2.7
# coding=UTF-8 

import optparse
import xlrd
import xlwt

class AccessXls:

	#构造函数不处理任何操作
	def __init__(self):
		pass

	#引入xls表
	def OpenFile(self,fileName):
		self.fileName = fileName

	#获取xls表列的数据
	def ReadMessageLine(self,line):        
		data = xlrd.open_workbook(self.fileName)
		table = data.sheet_by_name(u'Data')
		xlsLine = table.col_values(line)
		del xlsLine[0]
		return xlsLine

	#获取xls表有多少条数据
	def ReadMessageCount(self):        
		data = xlrd.open_workbook(self.fileName)
		table = data.sheet_by_name(u'Data')
		count = table.nrows - 1
		return count