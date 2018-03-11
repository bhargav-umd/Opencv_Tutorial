import cv2
import numpy as np

img = np.zeros([150,200,1],'uint8')
cv2.imshow("Image",img)

print(img[0,0,:])

img1 = np.ones([150,200,3],'uint8')
white = img1*255
cv2.imshow('ones',white)

red = img1.copy()
red[:,:] = (0,0,255)
cv2.imshow('redimagebhai',red)



cv2.waitKey()
#cv2.destroyAllWindows()
