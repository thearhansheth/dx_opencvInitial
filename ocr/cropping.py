import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample input images/cropImg.jpeg")
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(grayimg.shape)

img1 = img[130:1080, 110:800]
img2 = img[130:1050, 800:1380]

cv.imwrite("image_1.png", img1)
cv.imwrite("image_2.png", img2)
cv.imshow("Image 1", img1)
cv.imshow("Image 2", img2)
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()