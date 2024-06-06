import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/openCVlogo.jpeg")

blur = cv.blur(img, (5, 5))
gaus = cv.GaussianBlur(img, (5, 5), 0)
med = cv.medianBlur(img, 5)
bilat = cv.bilateralFilter(img, 9, 75, 75)

titles = ['Original Image', 'Averaging Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filtering']
images = [img, blur, gaus, med, bilat]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()