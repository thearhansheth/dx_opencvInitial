import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg", cv.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)

erosion = cv.erode(img, kernel, iterations = 1)
dilation = cv.dilate(img, kernel, iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
topHat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackHat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

titles = ['Original Image', 'Eroded Image', 'Dilated Image', 'Opening', 'Closing', 'Gradient', 'Top Hat', 'Black Hat']
images = [img, erosion, dilation, opening, closing, gradient, topHat, blackHat]

for i in range(8):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()