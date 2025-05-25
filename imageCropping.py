import cv2
import os
img = cv2.imread(os.path.join('.', 'data', 'image.png'))
cv2.imshow('img', img)
print(img.shape)
cropped_img = img[ 40:370 ,150 :450 ] # cropping the image from y1:y2, x1:x2 
print(cropped_img.shape)
cv2.imshow('cropped', cropped_img)
cv2.waitKey(0)