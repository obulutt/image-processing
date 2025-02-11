# -*- coding: utf-8 -*-

import cv2

"""
img = cv2.imread("example.jpg")

## açılacak olan pencereye isim verdik ve 
## açılacak olan resmi gönderdik
cv2.imshow("Faculty of Engineering", img)
cv2.waitKey(0)

""" 


"""
## açmak istediğimiz videoyu gönderdik
cap = cv2.VideoCapture("example.mp4")

## video biz q tuşuna basana kadar çalışması için while döngüsüne aldık
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""


## bir tane kameramız varsa laptopta örneğin 0 girerek varsayılan 
## olarak onun algılanmasını sağlarız

cam = cv2.VideoCapture(0)

## genişlik ve yükseklik boyutunu tanımladık 3 genişlik 4 yükseklik demek
cam.set(3,640)
cam.set(4,480)

## parlaklığı ayarlamak için de 10 id ile işlem yaparız
cam.set(10,100)
while True:
    success, img = cam.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

















