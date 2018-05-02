#!/usr/bin/python
# coding=UTF-8

'''Socket TCP客户端'''

import socket
import time, threading

#启动一个socket对象,连接9999端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#心跳维护
#s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

#连接服务端
s.connect(('127.0.0.1', 9999))

def tcpSend(sock):
	print("Please Input Your Message") 
	while True:
		# 发送数据:
		data = input("")
		sock.send(b"client:" + data.encode('utf-8'))

def tcpRece(sock):
	while True:
        #接收传输过来的数据
		data = sock.recv(1024)
		print(data.decode('utf-8'))

# 创建接收线程来处理TCP连接:
receThreading = threading.Thread(target=tcpRece, args=(s, ))
receThreading.start()

# 创建发送线程来处理TCP连接：
sendThreading = threading.Thread(target=tcpSend, args=(s, ))
sendThreading.start()