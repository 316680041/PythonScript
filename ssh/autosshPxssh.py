# coding=UTF-8
from pexpect import pxssh
def send_command(s, cmd):    
	s.sendline(cmd)    
	s.prompt()    
	print(s.before)
	
def connect(host, user, password):    
	try:        
		s = pxssh.pxssh()        
		s.login(host, user, password)        
		return s    
	except:        
		print('[-] Error Connecting')        
		exit(0)

def main():
	hostPath = input('请输入主机文件路径')
	cmd 	 = input('请输入要执行的命令')
	hostFile = open(hostPath, 'r')#打开密码文件
	for line in hostFile.readlines():
		user 	 = line.split(' ')[0]#获取用户名
		host 	 = line.split(' ')[1]#获取主机
		password = line.split(' ')[2]#获取密码
		child 	 = connect(host,user,password)
		send_command(child,cmd)

if __name__ == '__main__':
	main()