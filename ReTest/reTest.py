from PIL import Image
import pytesseract

def reTest():
	#上面都是导包，只需要下面这一行就能实现图片文字识别
	text=pytesseract.image_to_string(Image.open('reTest.jpg'),lang='chi_sim')
	print(text)

def main():
	reTest()

if __name__ == '__main__':    
	main()

