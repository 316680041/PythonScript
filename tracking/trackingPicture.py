# coding=UTF-8 
import optparse 
from PIL import Image 
from PIL.ExifTags import TAGS

#打印对象全部的属性
def prn_obj(obj): 
  print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

#查看图片里面的Exif数据是否有GPS位置，有则打印经纬度，没有则打印图片全部数据
def testForExif(imgFileName):    
	try:        
		exifData = {}        
		imgFile = Image.open(imgFileName)        
		info = imgFile._getexif()        
		if info:            
			for (tag, value) in info.items():                
				decoded = TAGS.get(tag, tag)                
				exifData[decoded] = value            
			exifGPS = exifData['GPSInfo']            
			if exifGPS:                
				print('[*] ' + imgFileName + ' contains GPS MetaData')
		else:
			prn_obj(imgFile)
	except:        
		pass

#主函数
def main():    
	parser = optparse.OptionParser('usage%prog -i <target image>')    
	parser.add_option('-i', dest='image', type='string', help='specify image address')    
	(options, args) = parser.parse_args()    
	image = options.image    
	if image == None:        
		print(parser.usage)        
		exit(0)    
	else:                  
		testForExif(image)

if __name__ == '__main__':    
	main()