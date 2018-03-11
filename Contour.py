
# coding: utf-8

# In[19]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[20]:


img = cv2.imread('Image2.jpeg',1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
adpt_thres=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('thresholded image',adpt_thres)


_, contours,hierarchy = cv2.findContours(adpt_thres, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index =-1 
thickness =4
color =(255,0,255)

#cv2.drawContours(img2,contours,index,color,thickness)
#cv2.imshow("Contours",img2)


# In[ ]:


objects = np.zeros([img.shape[0],img.shape[1],3],'uint8')

for c in contours:
    cv2.drawContours(objects,[c],-1,color,-1)


# In[ ]:




cv2.waitKey()
cv2.destroyAllWindows()

