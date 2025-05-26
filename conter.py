import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'black_birds.jpg'))
print(img.shape)
img = img[ 0:810 ,0 :1300 ]
img_tre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# we need to input in image with only one channel
ret ,img_tre = cv2.threshold(img_tre, 200, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(img_tre, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in contours:
    print(cv2.contourArea(i)) # print the area of each contour
    if cv2.contourArea(i) > 200:
        cv2.drawContours(img, [i], -1, (0, 250, 0), 1)
        x1, x2, w, h = cv2.boundingRect(i)
        cv2.rectangle(img, (x1, x2), (x1 + w, x2 + h), (0, 0, 255), 1)
cv2.imshow('image', img)   
cv2.imshow('image_tre', img_tre)
cv2.waitKey(0)