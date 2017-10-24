# coding=UTF-8

import os
import _winreg

'''
查看主机上用户已经删除的文件
'''

#查看回收站的路径
def returnDir():    
	dirs = ['C:\\$Recycle.Bin\\','C:\\Recycler\\', 'C:\\Recycled\\', ]    
	for recycleDir in dirs:        
		if os.path.isdir(recycleDir):
			return recycleDir
	return None

#根据sid去注册表查看用户名
def sid2user(sid):    
	try:        
		key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\" + sid)        
		(value, type) = _winreg.QueryValueEx(key, 'ProfileImagePath')        
		user = value.split('\\')[-1]        
		return user    
	except:        
		return sid

#把文件和用户名关联起来
def findRecycled(recycleDir):
	dirList = os.listdir(recycleDir)    
	for sid in dirList:        
		files = os.listdir(recycleDir + sid)        
		user = sid2user(sid)        
		print('\n[*] Listing Files For User: ' + str(user))        
		for file in files:            
			print('[+] Found File: ' + str(file))

#主函数
def main():
	recycledDir = returnDir() 
	findRecycled(recycledDir) 

if __name__ == '__main__':    
	main()