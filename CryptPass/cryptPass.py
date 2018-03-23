# coding=UTF-8
import optparse
from crypt import crypt

def testPass(dictPath,cryptSalt,cryptPass):
	dictFile = open(dictPath, 'r') #打开字典文件
	# while True:
	# 	block = dictFile.read(1024)#获取字典大小1024字节
	# 	if not block:
	# 		print('Password not found !')#匹配失败，返回
	# 		return
	for word in dictFile:#读取字典
		word = word.strip('\n') #保留原始的字符，不去空格
		print('Current progress is',word)
		cryptWord = crypt(word, cryptSalt)#获取字典的密码和盐结合
		if cryptPass == cryptWord:#匹配密码
			print('password is : ', word)#匹配成功输出解密后的密码，然后返回
			return

def main():
	parser = optparse.OptionParser('usage%prog '+'-p <passFile> -d <dictFile>')    
	parser.add_option('-p', dest='passFile', type='string', help='specify password file')    
	parser.add_option('-d', dest='dictFile', type='string', help='specify dictionary file')    
	(options, args) = parser.parse_args()    
	passFile = options.passFile
	dictFile = options.dictFile
	if passFile == None or dictFile == None:        
		print(parser.usage)        
		exit(0)   
	passFile = open(passFile, 'r')#打开密码文件
	for line in passFile.readlines():
		user = line.split(':')[0]#获取用户名
		if user=='root':
			cryptSalt = '$'+line.split('$')[1]+'$'+line.split('$')[2]#获取盐
			cryptPass = line.split(':')[1]#获取加密后的密码
			print("In cracking, please be patient...")
			testPass(dictFile,cryptSalt,cryptPass)
			return


if __name__=="__main__":
	main()
