import cv2
from cv2 import VideoCapture

cap = VideoCapture(2)
ret, frame = cap.read()
roi = cv2.selectROI(frame)

x, y, w, h = roi[0], roi[1], roi[2], roi[3]

cv2.destroyAllWindows()

while True:
    try:
        ret, frame = cap.read()
        # show_roi = frame[ y:y+h,x:x+w ]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.imshow('roi', frame) 
        key = cv2.waitKey(30)
    except key == ord('q'):
        break
    else:
        pass

cap.release()
cv2.destroyAllWindows()
