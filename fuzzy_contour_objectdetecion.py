import numpy as np
import cv2

bw = cv2.imread("fuzzy.png",0)
#binary = np.zeros(img.shape[0],img.shape[1],3,'unit8')*255
#img=cv2.adaptiveThreshold(bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

#kernel = np.ones((5,5),np.float32)/25
#img = cv2.filter2D(bw,-1,kernel)


median= cv2.medianBlur(bw,13)

img=cv2.adaptiveThreshold(median,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,131,1)

cv2.imshow('image',img)
_, contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index =-1 
thickness =4
color =(255,0,255)


objects = np.zeros([img.shape[0],img.shape[1],3],'uint8')

print(len(contours))

for c in contours:
    	area =cv2.contourArea(c)
	perimeters = cv2.arcLength(c,True)
	if area > 1000 and area < 40000:
		cv2.drawContours(objects,[c],-1,color,-1)
		cv2.imshow("contours",objects) 	
	        print("area :{} ,perimeter : {}".format(area,perimeters))


cv2.waitKey(0)
cv2.destroyAllWindows()
