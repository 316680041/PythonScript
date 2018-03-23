#!/usr/bin/python2.7
# coding=UTF-8 

'''该模块可以将自动化批量部署agent'''

__author__ = "jiegl"

import sys
import os
import optparse
sys.path.append("../libs")
import Common
from AccessXls import AccessXls
from Remote import Remote

#监控agent存放的目录
catalog = os.path.abspath(os.path.join(os.getcwd(), "../data/Linux_agent_minion"))

def main():

	parser = optparse.OptionParser('usage %prog -f <xls file name>')
	parser.add_option('-f', dest='fileName', type='string', help='specify xls file name')

	(options, args) = parser.parse_args()    
	fileName 	 = options.fileName

	if fileName == None:        
		print(parser.usage)        
		exit(0)
	else:
		accessXlsObj = AccessXls()
		remoteObj 	 = Remote()

		accessXlsObj.OpenFile(fileName)

		#获取ip和uuid
		ip 	 = accessXlsObj.ReadMessageLine(26)
		uuid = accessXlsObj.ReadMessageLine(1)
		count = accessXlsObj.ReadMessageCount()

		data = []

		#将数据提取到一个列表里面
		for value in range(count):
			tmp = {}
			tmp["ip"] 	= ip[0]
			tmp["uuid"] = uuid[0]
			del ip[0],uuid[0]
			data.append(tmp)

		for value in data:
			remoteObj.Connect(value["ip"],'root','')
			#下发目录到服务器集群里面
			os.system("scp -r " + catalog + " root@" + value["ip"] + ":/root/")
			#修改配置文件,server_ip的信息
			remoteObj.SendCommand('sed -i -e "s/server_ip =.*/server_ip = ' + value["ip"] + '/g"' + " /root/Linux_agent_minion/config.ini")
			remoteObj.SendCommand('sed -i -e "s/uuid =.*/uuid = ' + value["uuid"] + '/g"' + " /root/Linux_agent_minion/config.ini")
			remoteObj.SendCommand('cd /root/Linux_agent_minion && bash install.sh')	

if __name__ == '__main__':    
	main()