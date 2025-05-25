import os 
import cv2
# Canny Edge Detection
img = cv2.imread(os.path.join('.','data','runner.jpg')) # read the image
print(img.shape) 
img = cv2.resize(img, (600, 800)) # resize the image
img_edges = cv2.Canny(img, 100, 200) 
img = cv2.dilate(img_edges, None) 
cv2.imshow('original', img) # show the original image
cv2.imshow('edges', img_edges)
cv2.waitKey(0)
