import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    # Taking Each Frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # Define range of blue color in HSV
    lowerGreen = np.array([50, 100, 100])
    upperGreen = np.array([70, 255, 255])
    # Thresholding hsv image to get only blue colors 
    mask = cv.inRange(hsv, lowerGreen, upperGreen)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask = mask)
    # Displaying the image
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    # Wait Key
    k = cv.waitKey(5) & 0xFF
    if k == 5:
        break

cv.destroyAllWindows()
