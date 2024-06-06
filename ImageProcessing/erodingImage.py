import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/letters.png")
kernel = np.ones((5, 5), np.uint8)
#Try other ones

erodedImg = cv.erode(img, kernel, iterations = 2)

plt.subplot(121), plt.imshow(img), plt.title("Original Image")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(erodedImg), plt.title("Eroded Image")
plt.xticks([]), plt.yticks([])
plt.show()