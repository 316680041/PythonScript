# coding=UTF-8
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
			print('passed is : ', word)#匹配成功输出解密后的密码，然后返回
			return

def main():
	passPath = input('请输入密码文件路径')
	dictPath = input('请输入字典文件路径')
	passFile = open(passPath, 'r')#打开密码文件
	for line in passFile.readlines():
		user = line.split(':')[0]#获取用户名
		if user=='root':
			cryptSalt = '$'+line.split('$')[1]+'$'+line.split('$')[2]#获取盐
			cryptPass = line.split(':')[1]#获取加密后的密码
			print("In cracking, please be patient...")
			testPass(dictPath,cryptSalt,cryptPass)
			return


if __name__=="__main__":
	main()
