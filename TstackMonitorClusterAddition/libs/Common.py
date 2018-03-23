#!/usr/bin/python2.7
# coding=UTF-8 

import socket

#获取本机ip
def GetHostIp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

#替换配置文件
def ReplaceFile(file,beReplaced,replace):
	with open(file,'r') as r:
				lines=r.readlines()
	with open(file,'w') as w:
		for l in lines:
				w.write(l.replace(beReplaced,replace))