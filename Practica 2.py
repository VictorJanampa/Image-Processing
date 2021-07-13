#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
 
# Read the image
img1 = cv2.imread('Contrast2.PNG',0)
 
# Create zeros array to store the stretched image
minmax_img = np.zeros((img1.shape[0],img1.shape[1]),dtype = 'uint8')
limit_img = np.zeros((img1.shape[0],img1.shape[1]),dtype = 'uint8')
# Loop over the image and apply Min-Max formulae
minP=np.min(img1)
maxP=np.max(img1)
a=70
b=136
c=np.min(img1)
d=np.max(img1)
'''for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        minmax_img[i,j] = 255*(img1[i,j]-minP)/(maxP-minP)'''
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        limit_img[i,j] = (img1[i,j]-c)*(b-c)/(d-c)+a
        minmax_img[i,j] = 255*(img1[i,j]-minP)/(maxP-minP)

# Displat the stretched image
res = np.hstack((limit_img,minmax_img))
cv2.imshow('Minmax',res)
cv2.waitKey(0)


# In[ ]:





# In[ ]:




