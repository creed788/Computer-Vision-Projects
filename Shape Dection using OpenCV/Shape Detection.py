import cv2
import numpy as np

img  = cv2.imread('images/shapes.jpg')
img = cv2.resize(img, (600,500))
imgcontour = img.copy()

def getcontours(img):
  contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  for cnt in contours:
    area = cv2.contourArea(cnt)
    
    if area>500:
      print(area)
      cv2.drawContours(imgcontour, cnt, -1, (255,0,0), 3)
      para = cv2.arcLength(cnt, True)
      # print(para)
      approx = cv2.approxPolyDP(cnt, 0.02*para, True)
      objcor = len(approx)
      x, y, w, h = cv2.boundingRect(approx)

      cv2.rectangle(imgcontour, (x,y), (x+w, y+h), (0,255,0), 2)



imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggray,(7,7), 1)
imgblank = np.zeros_like(img)
imgcanny = cv2.Canny(imgblur, 50, 50)
getcontours(imgcanny)

cv2.imshow('gray', imggray)
cv2.imshow('blur', imgblur)
cv2.imshow('blank', imgcontour)
cv2.imshow('canny', imgcanny)



cv2.waitKey(0)
