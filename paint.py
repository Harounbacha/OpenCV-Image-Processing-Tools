import os
import cv2

# Paint application using OpenCV
img = cv2.imread(os.path.join('.', 'data', 'whiteboard.jpg'))  # Load a blank image
img = cv2.line(img, (300,200),(100,200) , (0,0,200), 9) # Draw a red line
img = cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 5)  # Draw a green rectangle
cv2.imshow('Paint', img)  # Display the image
cv2.waitKey(0)  # Wait for a key press