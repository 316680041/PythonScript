# 简介
 
常用Python脚本,每个目录为一个功能模块，环境为Python2.7或者3.6+，进入功能模块之后直接使用python 运行文件即可

# AutomationScript 模块

转换乱码的csv文件成xls文件+自动发送邮件

run.py 运行python脚本的文件

sendEmail.py 发送带附件的email

sendEmail2.py 发送简单的文字email

transCoding.py 将乱码的csv文件转换成为utf-8格式的xls文件

# CryptPass 模块

使用字典暴力破解unix密码文件,得出结果与服务器cpu运算速度有关

cryptPass.py 暴力破解unix密码文件

# DistributedQueue 模块

分布式队列+多线程执行任务

server.py 服务端,生成队列进程

client.py 客户端,从服务器进程中获取队列数据,执行并返回

insert.py 向服务器进程插入队列数据

# FTP 模块

ftpBrute.py ftp爆破账号密码

PasswordList.txt 爆破ftp账号密码的字典

# PDF 模块

pdfRead.py 提取pdf文件隐藏的数据(元数据)

# ReTest 模块

识别图片里面的文字，并提取出来

reTest.py 图片文字识别

reTest.jpg 要识别的图片

# RecycleBin 模块

查看主机上用户已经删除的文件

dumpRecycleBin.py 查看主机上用户已经删除的文件

注：该模块要用python2.7运行,python3运行会出错

# Scan 模块

Scan.py 扫描主机的端口是否存活(暂不可用)

ScanFtp.py 搜索主机的FTP服务是否可以匿名登录

ScanNamp.py 通过Nmap模块扫描主机端口是否存活(暂不可用)

# SSH 模块

autossh.py 通过ssh自动化运维，让多台服务器执行发布的命令(原生)

autosshPxssh.py 通过ssh自动化运维，让多台服务器执行发布的命令(优化版)

sshBrute.py 通过密码字典暴力破解远程ssh密码

sshBruteKey.py 通过密钥库暴力破解远程ssh密钥（弱密钥,暂不可用）

sshSession.py 建立ssh连接池，把客户机放入连接池里面，长时间控制客户机

#  Tracking模块

提取xls文件的ip和uuid批量执行安装监控Agent

trackingPicture.py 从图片中提取数据，查看图片是否有地理位置，有则打印，没有则打印图片全部属性

# TstackMonitorClusterAddition 模块

提取图片里面的隐藏数据

data 目录(数据信息目录)

|——Linux_agent_minion 监控Linux系统的Agent程序

libs 目录(功能模块目录)

|——AccessXls.py 提取xls文件的ip和uuid信息

|——Remote.py 远程执行代码

|——Common.py 公有函数

logs 目录(暂未开发)

|——暂无信息

sbin 目录(可执行程序目录)

|——run.py 运行python脚本的文件

# XmlDemo 模块

Python解析XML文件的demo

run.py 运行python脚本的文件

demo.xml 要解析的XML文件

# XmlTransitionXls 模块

获取服务器信息xml文件里面的数据，输入到xls文件里面

data 目录(数据信息目录)

|——bios 主板数据目录

|——cpu CPU数据目录

|——memory 内存数据目录

|——os 系统数据目录

libs 目录(功能模块目录)

|——parseXml.py 获取服务器信息xml文件里面的数据

|——transXlsx.py 将数据写入到xls文件里面

logs 目录(暂未开发)

|——暂无信息

sbin 目录(可执行程序目录)

|——run.py 运行python脚本的文件