import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(type(cap))
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()

    #Conversion of BGR TO HSV value
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Blue Color
    low = np.array([97,120,100])
    high = np.array([120, 255, 255])

    image_mask = cv2.inRange(hsv,low,high)
    # output = cv2.bitwise_and(frame,frame,mask=image_mask)
    # image_mask = cv2.inRange(image_mask,low, high)

    cv2.imshow('Tracked', image_mask)
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()

