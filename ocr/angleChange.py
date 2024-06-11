import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample input images/test_rotate.jpg")
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

smoothImg = cv.fastNlMeansDenoising(grayimg, h = 10)
T_, thresh = cv.threshold(smoothImg, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)
closingImage = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=5)
rows, cols = grayimg.shape
print(grayimg.shape)
print(closingImage)

#height, width = closingImage.shape[:2]
#res = cv.resize(closingImage, (width, height), interpolation = cv.INTER_CUBIC)

M = cv.getRotationMatrix2D(((cols - 1)/2.0, (rows - 1)/2.0), 5, 1)
rotated = cv.warpAffine(img, M, (cols, rows))
print(rotated.shape)

final = rotated[1000:5900, 1400:7800]

cv.imshow("Final", closingImage)
cv.imshow("Rotated", rotated)
cv.imshow("Final v2", final)
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()