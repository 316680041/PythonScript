# coding=UTF-8

import optparse 
from pexpect import pxssh

botNet = []#创建连接池

#连接客户端主机的类
class Client:
	def __init__(self, host, user, password):        
		self.host = host        
		self.user = user        
		self.password = password        
		self.session = self.connect()  
	def connect(self):        
		try:            
			s = pxssh.pxssh()            
			s.login(self.host, self.user, self.password)            
			return s        
		except Exception as e:            
			print(e)            
			print('[-] Error Connecting')  
	def send_command(self, cmd):        
		self.session.sendline(cmd)        
		self.session.prompt()        
		return self.session.before

#遍历连接池执行命令，然后输出执行结果
def botnetCommand(command):    
	for client in botNet:        
		output = client.send_command(command)        
		print('[*] Output from ' + client.host)        
		print('[+] ' + str(output) + '\n')

#连接主机，然后添加到连接池里面
def addClient(host, user, password):    
	client = Client(host, user, password)    
	botNet.append(client)

#主函数
def main():
	botNet = []#创建连接池
	addClient('172.25.24.10', 'root', 'password') 
	addClient('172.25.24.20', 'root', 'password') 
	addClient('172.25.24.30', 'root', 'password') 
	botnetCommand('uname -v') #遍历连接池执行命令
	botnetCommand('netstat -ntlp')

if __name__ == '__main__':
	main()


