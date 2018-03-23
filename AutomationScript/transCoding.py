#!/usr/bin/python2.7
# coding=UTF-8 

import optparse
import csv
import xlwt

class transCoding:
	def __init__(self, fileName, saveFile):        
		self.fileName = fileName        
		self.saveFile = saveFile
	def start(self):        
		csv_file = csv.reader(open(self.fileName,'r'))
		myexcel = xlwt.Workbook(encoding='utf-8')
		mysheet = myexcel.add_sheet("zabbix")
		tmp = []
		for i in csv_file:
		    tmp.append(i)
		for line in range(len(tmp)):
		    for split_line in tmp[line]:
		        data = split_line.split("\t")
		        print(data)
		        for column in range(len(data)):
		            mysheet.write(line,column,data[column])
		myexcel.save(self.saveFile)

if __name__ == '__main__':    
	main()