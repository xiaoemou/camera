# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:14:24 2018

@author: SEELE
"""

#from PIL import Image
#import numpy as np
#im=Image.open("C:\\Users\\Public\\Pictures\\Sample Pictures\\001.jpg")
#im.show()
#im_array = np.array(im)
#print(im_array.shape)
import cv2
img=cv2.imread("C:\\Users\\Public\\Pictures\\Sample Pictures\\001.bmp")
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img3=cv2.resize(img2,(28,28))
img2=img3.reshape(-1,28,28,1)
#img3=cv2.resize(img2,(1200,900))
#cv2.imshow("image",img3)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()