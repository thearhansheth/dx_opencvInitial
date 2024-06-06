import numpy as np
import cv2 as cv
 
img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/cages.png")
assert img is not None, "file could not be read, check with os.path.exists()"
ogImage = img.copy()
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 140, 255, 0)
ret2, thresh2 = cv.threshold(imgray, 65, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0, 255, 0), 2)
cv.drawContours(img, contours2, -1, (0, 255, 0), 2)

cv.imshow("Result", img)
cv.imshow("Original Image", ogImage)
cv.waitKey(0)
cv.destroyAllWindows()