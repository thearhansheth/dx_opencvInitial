import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg")

if len(img.shape) == 2:  # Grayscale image
    rows, cols = img.shape
elif len(img.shape) == 3:  # Color image
    rows, cols, channels = img.shape

# Coordinate Limits
m = cv.getRotationMatrix2D(((cols - 1)/2.0, (rows - 1)/2.0), 90, 1)
res = cv.warpAffine(img, m, (cols, rows))

# Display Images 
cv.imshow("Original Image", img)
cv.imshow("Rotated Image", res)
cv.waitKey(0)
cv.destroyAllWindows()