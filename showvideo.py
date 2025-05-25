import cv2
import os

# read video and show it in a window

# read video
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
cv2.destroyAllWindows()