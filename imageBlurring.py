import cv2
import os

# image blurring
# in blurring we use gaussian blur to remove noise from the image
# there is many types of blurring like median blur, bilateral blur, etc
# GO TO the documentation in "https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html" for more information
img = cv2.imread(os.path.join('.','data','men.jfif'))
img = cv2.resize(img, (500, 500,))
k_Size = 9  # kernel size
img_blur = cv2.blur(img, (k_Size,k_Size), 0)
img_median = cv2.medianBlur(img, 9)  # median blur
img_noisy = cv2.imread(os.path.join('.','data','noisy.jpg'))
img_blur_noisy = cv2.blur(img_noisy, (k_Size,k_Size), 0)
img_median_noisy = cv2.medianBlur(img_noisy, 5)  # median blur
img_gaussian_noisy = cv2.GaussianBlur(img_noisy, (k_Size,k_Size), 0)  # gaussian blur
cv2.imshow('original', img)
cv2.imshow('blurred', img_blur)
cv2.imshow('blurred_median', img_median)
cv2.imshow('noisy', img_noisy)
cv2.imshow('blurred_noisy', img_blur_noisy)
cv2.imshow('blurred_median_noisy', img_median_noisy)
cv2.imshow('blurred_gaussian_noisy', img_gaussian_noisy)
cv2.waitKey(0)