import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg")
kernel = np.ones((5, 5), np.float32)/25
res = cv.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title("Original Image")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(res), plt.title("Filtered Image")
plt.xticks([]), plt.yticks([])
plt.show()