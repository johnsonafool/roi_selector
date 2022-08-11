import cv2
from cv2 import VideoCapture

cap = VideoCapture(2)
ret, frame = cap.read()
roi = cv2.selectROI(frame)
print(roi)
cv2.destroyAllWindows()

while True:
    try:
        ret, frame = cap.read()
        cv2.imshow('roi', frame) 
    
        key = cv2.waitKey(30)
    except key == ord('q'):
        break
    else:
        pass

cap.release()
cv2.destroyAllWindows()
