import os
import cv2
 # read image -------------------------------------
image_path = os.path.join('.','data','image.png')

img = cv2.imread(image_path)

# write image -------------------------------------

write_path = os.path.join('.','data','image_out.png')
cv2.imwrite(write_path, img)

# show image or visualize -------------------------

cv2.imshow('frame', img)
cv2.waitKey(0) 
----------------------------------------------------