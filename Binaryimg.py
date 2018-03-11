
# coding: utf-8

# In[17]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

bw = cv2.imread('Image3.jpeg',0)
cv2.imshow('bwimage',bw)


# In[18]:


h,w = bw.shape[0:2]

binary = np.zeros([h,w,1],'uint8')
thresh = 70

for r in range(0,h):
    for c in range(0,w):
        binary[r][c]= 255 if bw[r][c] > thresh else 0
        
cv2.imshow('binaryre',binary)

ret,f =cv2.threshold(bw,45,255,cv2.THRESH_BINARY)
cv2.imshow('naya',f)


# In[19]:


adpt_thres=cv2.adaptiveThreshold(bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('sabse naya',adpt_thres)


# In[20]:


cv2.waitKey(0)
cv2.destroyAllWindows()

