import os 
import cv2

# Threshold 
img = cv2.imread(os.path.join('.','data','scarface.jpg')) # read the image
print(img.shape)
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to gray scale
ret ,threshold = cv2.threshold(image_gray,50 ,255,cv2.THRESH_BINARY) # apply thresholding
threshold = cv2.resize(threshold, (600,800)) 
img = cv2.resize(img, (600,800)) #
cv2.imshow('original', img)
cv2.imshow('threshold', threshold) # show the thresholded image
cv2.waitKey(0)