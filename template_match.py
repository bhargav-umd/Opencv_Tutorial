import cv2
import numpy as np 

frame = cv2.imread('players.jpg',0)
template = cv2.imread('template.jpg',0)

cv2.imshow('frames',frame)
cv2.imshow('templatess',template)

result = cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)
min ,max ,min_loc,max_loc =cv2.minMaxLoc(result)
print('max value is : {} and max location is: {}'.format( max,max_loc))
cv2.circle(result,max_loc,15,255,2)
cv2.imshow('matching',result)




cv2.waitKey(0)
cv2.destroyAllWindows()
