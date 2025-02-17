# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("example.jpg")

"""
width,height =250,350
## belirlediğimiz bir alanı kesip almaya yarıyor
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("img",img)
cv2.imshow("New Img", imgOutput)
"""

## iki resmi yanyana birleştirme
imgHor = np.hstack((img,img))

## iki resmi alt alta birleştirme
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)


