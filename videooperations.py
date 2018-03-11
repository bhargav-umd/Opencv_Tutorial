
# coding: utf-8

# In[29]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[30]:


#cap =cv2.VideoCapture('challenge_video.mp4')
cap =cv2.VideoCapture(0)

color = (255,0,0)
linewidth = 2
point = (0,0)
radius = 30





# In[31]:


def click(event,x,y,flags,param):
    global point,pressed
    
    if event ==cv2.EVENT_LBUTTONDOWN:
        print("pressed",x,y)
        point =(x,y)
cv2.namedWindow("awesomeness with circle")
cv2.setMouseCallback("awesomeness with circle",click)


# In[32]:



while(cap.isOpened()):
    ch = cv2.waitKey(1)
    ret , frame = cap.read()
    frame = cv2.resize(frame, (0,0),fx=0.5,fy=0.5)

    cv2.circle(frame,point,radius,color,linewidth)
    #gray_image = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cv2.imshow("awesomeness with circle",frame)
    
    if ch & 0xFF ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

