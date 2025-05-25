import cv2
import os

img_resize =cv2.imread(os.path.join('.','data','image.png'))
print(img_resize.shape)
cv2.imshow('original',img_resize)
img_resize = cv2.resize(img_resize, (1148, 774,))
print(img_resize.shape)
cv2.imshow('resize',img_resize)
cv2.waitKey(0)