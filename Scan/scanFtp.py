# coding=UTF-8
import ftplib
import optparse

'''
扫描ftp服务器是否可以匿名登录
'''

def anonLogin(hostname):    
	try:        
		ftp = ftplib.FTP(hostname)        
		ftp.login('anonymous','')        
		print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded!')        
		ftp.quit()        
		return True    
	except Exception as e:        
		print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed!')        
		return False

def main():
	parser = optparse.OptionParser('usage%prog '+'-H <host>')    
	parser.add_option('-H', dest='host', type='string', help='specify host')     
	(options, args) = parser.parse_args()    
	host = options.host
	if host == None:        
		print(parser.usage)        
		exit(0)
	anonLogin(host)


if __name__ == '__main__':
	main()