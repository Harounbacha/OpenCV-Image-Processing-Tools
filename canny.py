import os 
import cv2
# Canny Edge Detection
img = cv2.imread(os.path.join('.','data','runner.jpg')) # read the image
print(img.shape) 
img_edges = cv2.Canny(img, 100, 200) 
cv2.imshow('original', img) # show the original image
cv2.imshow('edges', img_edges)
cv2.waitKey(0)
