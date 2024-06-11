import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample input images/cropImg.jpeg")
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)