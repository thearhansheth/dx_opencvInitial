import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg", cv.IMREAD_GRAYSCALE)

rows, cols = img.shape
tr = np.float32([[1, 0, 100], [0, 1, 50]])
res = cv.warpAffine(img, tr, (cols, rows))

cv.imshow("OpenCV", img)
cv.imshow("Resulting Image", res)

cv.waitKey(0)
cv.destroyAllWindows()