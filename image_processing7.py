# -*- coding: utf-8 -*-

import cv2
import numpy as np 

path = "shapes.png"

img =cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

cv2.imshow("Original IMG", img)
cv2.imshow("Gray IMG", imgGray)
cv2.imshow("Blur IMG", imgBlur)
cv2.waitKey(0)


