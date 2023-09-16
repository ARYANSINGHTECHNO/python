import cv2   # library
import numpy as np

CAM_IDX = 0        # 0: default camera
cam = cv2.VideoCapture(CAM_IDX)

while cam.isOpened():
    state, frame = cam.read()
    if not state:
        print('Camera is not available')
        break
    # modification
    frame = cv2.flip(frame, 1)           # Mirror image
    # modification till here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    outline = cv2.Canny(gray,100,110)             #img,min,max
    img = np.hstack([gray, outline])
    # drawing
    img = cv2.putText(img, "GRAY IMAGE",(300, 40),
                      cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    img = cv2.putText(img, "CANNY IMAGE",(1280-300, 40),
                      cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) == 27:           # ESC KEY
        break
cam.release()
cv2.destroyAllWindows()