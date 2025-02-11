# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("example.jpg")
kernel = np.ones((5,5),np.uint8)

## resmimizi önce griye çevirdik
## resmi blurlayıp gri hali ile arasındaki farkı görüyoruz
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)

## kenar belirleme için canny kullandık
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("Canny", imgCanny)

imgDialation = cv2.dilate(imgCanny, kernel,iterations=1)
cv2.imshow("Dialation", imgDialation)

imgEroded = cv2.erode(imgDialation,kernel, iterations=1)
cv2.imshow("Eroded", imgEroded)
cv2.waitKey(0)
