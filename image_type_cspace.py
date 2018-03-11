import cv2
import numpy as np



color =cv2.imread('Image1.jpeg') #default , 1 as color image
cv2.imshow("Imag", color)
cv2.moveWindow("imag",0,0)

height,width,channels = color.shape
print(color.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

