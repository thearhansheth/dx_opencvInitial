import numpy as np
import cv2 as cv
import math

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/red_shape.png")
if img is None:
    print("Error")
    exit(1)
gimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cImg = cv.cvtColor(gimg, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(gimg, cv.HOUGH_GRADIENT, 1, 20, param1 = 100, param2 = 45, minRadius = 0, maxRadius = 0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv.circle(cImg, (i[0], i[1]), i[2],(0,255,0),2)

cv.imshow("Original Image", img)
cv.imshow("Result", cImg)
cv.waitKey(0)
cv.destroyAllWindows()