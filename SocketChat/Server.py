#!/usr/bin/python
# coding=UTF-8

'''Socket TCP服务端'''

import socket
import time, threading

#启动一个socket对象,监听9999端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))

#调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)

print('Waiting for connection...')

def tcplink(sock, addr): 
    print('Accept new connection from %s:%s...' % addr)

def tcpSend(sock, addr):
	print("Please Input Your Message") 
	while True:
		# 发送数据:
		data = input("")
		sock.send(b"server:" + data.encode('utf-8'))

def tcpRece(sock, addr):
	while True:
        #接收传输过来的数据
		data = sock.recv(1024)
		print(data.decode('utf-8'))

while True:
    # 接受TCP连接并返回（sock,address）,其中sock是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
    sock, addr = s.accept()

    # 创建接收线程来处理TCP连接:
    receThreading = threading.Thread(target=tcpRece, args=(sock, addr))
    receThreading.start()

    # 创建发送线程来处理TCP连接：
    sendThreading = threading.Thread(target=tcpSend, args=(sock, addr))
    sendThreading.start()