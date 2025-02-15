# -*- coding: utf-8 -*-

import cv2

img = cv2.imread("example.jpg")

## resmimizin boyutlarını görüyoruz
print(img.shape)

## resmimizi tekrar şekillendiriyoruz
imgResize = cv2.resize(img, (200,300))


## ilk yazdığımız koordinat yükseklik için ikincisi genişlik için
imgCropped = img[0:200,0:400]


cv2.imshow("Resize Img", imgResize)
cv2.imshow("Img", img)
cv2.imshow("Cropped Img", imgCropped)
cv2.waitKey(0)

