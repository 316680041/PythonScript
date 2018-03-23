#!/usr/bin/python2.7
# coding=UTF-8 

'''该模块负责提取xml数据'''

__author__ = "jiegl"

import xml.dom.minidom

class parseXml:
	def __init__(self):
		self.dom = "" 

	def setPath(self,xmlName):
		self.dom = xml.dom.minidom.parse(xmlName)

	def extract(self,tagName,attribute,findName):
		root = self.dom.documentElement
		itemlist = root.getElementsByTagName(tagName)
		for item in itemlist:
			if item.getAttribute(attribute) == findName :
				return item.firstChild.data

	def extractCount(self,tagName,attribute,findName):
		i = 0
		root = self.dom.documentElement
		itemlist = root.getElementsByTagName(tagName)
		for item in itemlist:
			if item.getAttribute(attribute) == findName :
				i += 1
		return i