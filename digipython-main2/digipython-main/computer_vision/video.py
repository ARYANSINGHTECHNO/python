import cv2   # library
import numpy as np

VIDEO_PATH = r"C:\Users\Asus\Downloads\Vinland Saga\[Cerberus] Vinland Saga - S01E01 - [F7B9EB8F].mkv"# 0: default camera
cam = cv2.VideoCapture(VIDEO_PATH)

while cam.isOpened():
    state, frame = cam.read()
    if not state:
        print('Camera is not available')
        break
    frame = cv2.resize(frame, None, fx=.5, fy=.5)
    cv2.imshow('video', frame)
    if cv2.waitKey(10) == 27:           # ESC KEY
        break
cam.release()
cv2.destroyAllWindows()