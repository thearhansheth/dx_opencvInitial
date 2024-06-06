import numpy as np
import cv2 as cv
import math

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/shapes.jpg")
ogImg = img.copy()
if img is None:
    print("Error")
    exit(1)
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

res, th = cv.threshold(grayImg, 127, 255, 0)
contours, heirarcy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for i in range(4):
    cnt = contours[i]
    perimeter = cv.arcLength(cnt, True)
    print("Perimeter:", perimeter)
    s = int(perimeter / 4)
    print("Square Root:", s)
    if ((s * 4) == perimeter):
        print("Found Square")
        cv.drawContours(img, contours, i, (0, 255, 0), 3)

cv.imshow("Original Image", ogImg)
cv.imshow("Contoured Image", img)
cv.waitKey(0)
cv.destroyAllWindows()

