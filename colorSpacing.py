#color spacing
import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'image2.jfif')) # read the image
print(img.shape)
resize_img = cv2.resize(img, (368, 556,)) # resizing the image to 368x556
cv2.imshow('BGR', resize_img)
rgbImage = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB) # convert to RGB
greyImage = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY) # convert to grey scale
hsvImage = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV) # convert to HSV
cv2.imshow('RGB', rgbImage)
cv2.imshow('GREY', greyImage)
cv2.imshow('HVS', hsvImage) 

cv2.waitKey(0)