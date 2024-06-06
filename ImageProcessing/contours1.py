import numpy as np
import cv2 as cv

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/hand.jpeg")
img2 = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/desk.jpeg")
if img is None:
    print("Error")
    exit(1)

grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayImg2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

res, th = cv.threshold(grayImg, 127, 255, 0)
res2, th2 = cv.threshold(grayImg2, 127, 255, 0)

contours, hierarchy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours2, heirarchy2 = cv.findContours(th2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#cnt = contours[144]
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.drawContours(img2, contours2, -1, (0, 255, 0), 2)

cv.imshow("Original Image", grayImg)
cv.imshow("Contoured Image", img)
cv.imshow("Original Image 2", grayImg2)
cv.imshow("Contoured Image 2", img2)
cv.waitKey(0)
cv.destroyAllWindows()


