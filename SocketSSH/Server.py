# !/usr/bin/python
# coding=UTF-8 

'''SocketSSH服务端'''

__author__ = "jiegl"

import socket
import pika
import time, threading

#启动一个socket对象,监听9999端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))

#socket列表
socketList = []

#连接rabbitmq
credentials = pika.PlainCredentials('admin','123456')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.199.246',5672,'/',credentials))
channel = connection.channel()

#在两个程序中重复声明队列。
channel.queue_declare(queue='Code',durable=True)

#调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)

#打印连接过来的主机
def tcplink(sock, addr): 
    print('Accept new connection from %s:%s...' % addr)

#rabbitmq接受到数据后的处理函数
def callback(ch, method, properties, body):
    for sock in socketList:
        sock["sock"].send(body.encode('utf-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)

#线程函数
def tcpSend(sock, addr):
	channel.basic_consume(callback,queue='Code',)
	channel.start_consuming()

while True:
    # 接受TCP连接并返回（sock,address）,其中sock是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
    sock, addr = s.accept()

    tmp = {}
    tmp["sock"] = sock
    tmp["addr"] = addr
    socketList.append(tmp)

    # 创建发送线程来处理TCP连接：
    sendThreading = threading.Thread(target=tcpSend, args=(sock, addr))
    sendThreading.start()
