# coding=UTF-8
import pexpect
import optparse
PROMPT = ['# ', '>>> ', '> ', '\$ '] 

#执行命令模块
def send_command(child, cmd):
	child.sendline(cmd)    
	child.expect(PROMPT)
	print(child.before)
#连接模块
def connect(user, host, password):    
	ssh_newkey = 'Are you sure you want to continue connecting'    
	connStr = 'ssh ' + user + '@' + host    
	child = pexpect.spawn(connStr)    
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])    
	if ret == 0:        
		print('[-] Error Connecting')        
		return    
	if ret == 1:        
		child.sendline('yes')        
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])    
	if ret == 0:        
		print('[-] Error Connecting')        
		return    
	child.sendline(password)    
	child.expect(PROMPT)    
	return child

def main():
	parser = optparse.OptionParser('usage%prog '+'-H <hostFile> -m <cmd>')    
	parser.add_option('-H', dest='hostFile', type='string', help='specify host file')    
	parser.add_option('-m', dest='cmd', type='string', help='specify cmd')    
	(options, args) = parser.parse_args()    
	hostFile = options.hostFile
	cmd 	 = options.cmd
	if hostFile == None or cmd == None:        
		print(parser.usage)        
		exit(0)  
	hostFile = open(hostFile, 'r')#打开密码文件
	for line in hostFile.readlines():
		user 	 = line.split(' ')[0]#获取用户名
		host 	 = line.split(' ')[1]#获取主机
		password = line.split(' ')[2]#获取密码
		child 	 = connect(user,host,password)
		send_command(child,cmd)
		


if __name__ == '__main__':
	main()