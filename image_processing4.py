# -*- coding: utf-8 -*-

import cv2
import numpy as np

## siyah bir ekran oluştururuz bu şekilde 
img = np.zeros((512,512))

## oluşan siyah ekranın belirli bir bölgesine farklı renk eklemek için kullanılır
newImg = np.zeros((512,512,3),np.uint8)
newImg[200:300,100:300] = 255,0,0

## istediğimiz bir resme başlangıç, bitiş ve renk kodu vererek çizgi ekleyebiliriz
cv2.line(newImg, (0,0), (300,300), (0,255,0),3)
secimg =  np.zeros((512,512,3),np.uint8)

## resme bir dikdörtgen ekledik, içini komple doldurmak yerine sayı vererek kalınlık da belirtebiliriz
cv2.rectangle(secimg, (0,0), (250,350),(0,0,255),cv2.FILLED)

## daire çizdik
cv2.circle(secimg, (400,50), 30, (255,255,0),8)

cv2.putText(secimg, "hello", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0))

cv2.imshow("Sec Img", secimg)
cv2.imshow("New Img",newImg)
cv2.imshow("image", img)
cv2.waitKey(0)