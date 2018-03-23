# coding=UTF-8
from pexpect import pxssh
import optparse
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
		child 	 = connect(host,user,password)
		send_command(child,cmd)

if __name__ == '__main__':
	main()