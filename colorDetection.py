import cv2
import os
from PIL import Image
from utils import get_limits


yallow = (0, 255, 255)  # BGR format for yellow color

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("filed to capture video")
    exit()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yallow)
    mask = cv2.inRange(
       hsvImage,lowerLimit, upperLimit
    )

    mask_ = Image.fromarray(mask)
    bbox  = mask_.getbbox()
    print(bbox)
    cv2.imshow('frame', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    

    