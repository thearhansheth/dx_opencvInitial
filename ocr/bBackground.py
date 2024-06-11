import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample input images/input.jpeg")
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
res, thresh = cv.threshold(grayimg, 0, 255, cv.THRESH_BINARY)

