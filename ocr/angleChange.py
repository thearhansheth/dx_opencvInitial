import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample input images/test_rotate.jpg", cv.IMREAD_GRAYSCALE)
rows, cols = img.shape

M = cv.getRotationMatrix2D(((cols - 1)/2.0, (rows - 1)/2.0), 5, 1)
res = cv.warpAffine(img, M, (rows, cols))

cv.imshow("Result", res)
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()