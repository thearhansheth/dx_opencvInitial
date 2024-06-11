import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample input images/input.jpeg")
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
res, thresh = cv.threshold(grayimg, 0, 255, cv.THRESH_BINARY)

edges = cv.Canny(thresh, 100, 200)
lines = cv.HoughLinesP(edges, 1, np.pi/180,100, minLineLength = 100, maxLineGap = 10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img, (x1,y1), (x2,y2), (0, 255, 0), 4)

cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()
