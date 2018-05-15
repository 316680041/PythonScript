# !/usr/bin/python
# coding=UTF-8 

'''把命令插入rabbitmq队列'''

__author__ = "jiegl"

import pika

credentials = pika.PlainCredentials('admin','123456')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.199.246',5672,'/',credentials))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='Code',durable=True)

# RabbitMQ消息不能直接发送到队列，它总是需要通过交换。
channel.basic_publish(exchange='',
                      routing_key='Code',
                      body='touch /root/demo.txt',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                      )
print(" [x] Sent 'ok'")
connection.close()
