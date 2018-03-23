# coding=UTF-8 
import PyPDF2 
from PyPDF2 import PdfFileReader 
import optparse

'''
查看PDF文件隐藏的数据
'''

#传递文件路径，然后打开该文件，调用getDocumentInfo函数查看PDF隐藏得数据
def printMeta(fileName):
	pdfFile = PdfFileReader(open(fileName, 'rb'))    
	docInfo = pdfFile.getDocumentInfo()    
	print('[*] PDF MetaData For: ' + str(fileName))    
	for metaItem in docInfo:        
		print('[+] ' + metaItem + ':' + docInfo[metaItem]) 

#主函数
def main():    
	parser = optparse.OptionParser('usage %prog -F <PDF file name>')    
	parser.add_option('-F', dest='fileName', type='string', help='specify PDF file name')    
	(options, args) = parser.parse_args()    
	fileName = options.fileName    
	if fileName == None:        
		print(parser.usage)        
		exit(0)    
	else:        
		printMeta(fileName)

if __name__ == '__main__':    
	main()