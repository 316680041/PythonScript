# 简介
 
常用Python脚本,每个目录为一个功能模块，环境为Python3.6+，进入功能模块之后直接使用python 运行文件即可。

# cryptPass 模块

使用字典暴力破解unix密码文件,得出结果与服务器cpu运算速度有关。

# Scan 模块

Scan.py 扫描主机的端口是否存活(暂不可用)

ScanFtp.py 搜索主机的FTP服务是否可以匿名登录

ScanNamp.py 通过Nmap模块扫描主机端口是否存活(暂不可用)

# ssh 模块

autossh.py 通过ssh自动化运维，让多台服务器执行发布的命令。(原生)

autosshPxssh.py 通过ssh自动化运维，让多台服务器执行发布的命令。(优化版)

sshBrute.py 通过密码字典暴力破解远程ssh密码

sshBruteKey.py 通过密钥库暴力破解远程ssh密钥（弱密钥,暂不可用）

sshSession.py 建立ssh连接池，把客户机放入连接池里面，长时间控制客户机。

# 分布式队列+多线程 模块

server.py 服务端,生成队列进程

client.py 客户端,从服务器进程中获取队列数据,执行并返回

insert.py 向服务器进程插入队列数据