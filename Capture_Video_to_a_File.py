import numpy as np
import cv2

# Capture one frame and save it to file
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite("frame.jpg", frame)
cap.release()