import os
import cv2

# here is the all functions in one file 
 # read image 
""""
image_path = os.path.join('.','data','image.png')

img = cv2.imread(image_path)

# write image 
write_path = os.path.join('.','data','image_out.png')
cv2.imwrite(write_path, img)
# show image or visualize
cv2.imshow('frame', img)
cv2.waitKey(0)  """

 # read video and show it in a window

""" # read video
video_path = os.path.join('.','data','video.mp4')
video = cv2.VideoCapture(video_path)

# show video or visualize

bool = True
while bool  :
    bool , frame = video.read()

    cv2.imshow('frame', frame)
    cv2.waitKey(40)  # 25 fps
    if cv2.waitKey(1) != -1:     # if any key is pressed kill the video
        print('Key pressed, exiting video playback.')
        break
    
video.release()
cv2.destroyAllWindows() """

# basic image operations
# image resizing
""" img_resize =cv2.imread(os.path.join('.','data','image.png'))
print(img_resize.shape)
cv2.imshow('original',img_resize)
img_resize = cv2.resize(img_resize, (1148, 774,))
print(img_resize.shape)
cv2.imshow('resize',img_resize)
cv2.waitKey(0)

 """
# image cropping

""" img = cv2.imread(os.path.join('.', 'data', 'image.png'))
cv2.imshow('img', img)
print(img.shape)
cropped_img = img[ 40:370 ,150 :450 ]
print(cropped_img.shape)
cv2.imshow('cropped', cropped_img)
cv2.waitKey(0) """

# color spacing

""" img = cv2.imread(os.path.join('.', 'data', 'image2.jfif'))
print(img.shape)
resize_img = cv2.resize(img, (368, 556,))
cv2.imshow('BGR', resize_img)
rgbImage = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)
greyImage = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
hsvImage = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)
cv2.imshow('RGB', rgbImage)
cv2.imshow('GREY', greyImage)
cv2.imshow('HVS', hsvImage) 

cv2.waitKey(0) """

# image blurring
# in blurring we use gaussian blur to remove noise from the image
# there is many types of blurring like median blur, bilateral blur, etc
# GO TO the documentation in "https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html" for more information
"""
img = cv2.imread(os.path.join('.','data','men.jfif'))
img = cv2.resize(img, (500, 500,))
k_Size = 9  # kernel size
img_blur = cv2.blur(img, (k_Size,k_Size), 0)
img_median = cv2.medianBlur(img, 9)  # median blur
img_noisy = cv2.imread(os.path.join('.','data','noisy.jpg'))
img_blur_noisy = cv2.blur(img_noisy, (k_Size,k_Size), 0)
img_median_noisy = cv2.medianBlur(img_noisy, 5)  # median blur
img_gaussian_noisy = cv2.GaussianBlur(img_noisy, (k_Size,k_Size), 0)  # gaussian blur
img_median_noisy2 = os.path.join('.','data','img_median_noisy.jpg')
cv2.imwrite(img_median_noisy2, img)
""" cv2.imshow('original', img)
cv2.imshow('blurred', img_blur)
cv2.imshow('blurred_median', img_median) """
cv2.imshow('noisy', img_noisy)
cv2.imshow('blurred_noisy', img_blur_noisy)
cv2.imshow('blurred_median_noisy', img_median_noisy)
cv2.imshow('blurred_gaussian_noisy', img_gaussian_noisy)

cv2.waitKey(0)
"""

