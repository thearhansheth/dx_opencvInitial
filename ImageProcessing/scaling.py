import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg")

height, width = img.shape[:2]
res = cv.resize(img, (2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.imshow('Image', img)
cv.imshow('Resulting Resize', res)
cv.waitKey(0)
cv.destroyAllWindows()