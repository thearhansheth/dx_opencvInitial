import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg")
print(img.shape)
cv.imshow("OpenCV Logo", img)

cv.waitKey(0)
cv.destroyAllWindows()