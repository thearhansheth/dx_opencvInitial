import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg")
canny = cv.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img), plt.title("Original Image")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(canny), plt.title("Canny Edge Detected Image")
plt.xticks([]), plt.yticks([])
plt.show()