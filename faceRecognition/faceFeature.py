from PIL import Image, ImageDraw
import optparse
import face_recognition
'''
打印脸部特征轮廓
'''
def faceFeature(picture):
	# 将jpg文件加载到numpy 数组中
	image = face_recognition.load_image_file(picture)

	# 查找图像中所有面部的所有面部特征
	face_landmarks_list = face_recognition.face_landmarks(image)

	print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

	for face_landmarks in face_landmarks_list:

	   #打印此图像中每个面部特征的位置
	    facial_features = [
	        'chin',
	        'left_eyebrow',
	        'right_eyebrow',
	        'nose_bridge',
	        'nose_tip',
	        'left_eye',
	        'right_eye',
	        'top_lip',
	        'bottom_lip'
	    ]

	    for facial_feature in facial_features:
	        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

	   #让我们在图像中描绘出每个人脸特征！
	    pil_image = Image.fromarray(image)
	    d = ImageDraw.Draw(pil_image)

	    for facial_feature in facial_features:
	        d.line(face_landmarks[facial_feature], width=5)

	    pil_image.show()

def main():
	parser = optparse.OptionParser('usage%prog '+'-p <picture>')    
	parser.add_option('-p', dest='picture', type='string', help='specify picture file')    
	(options, args) = parser.parse_args()    
	picture = options.picture
	if picture == None:        
		print(parser.usage)        
		exit(0)
	faceFeature(picture)

if __name__ == '__main__':
	main()
