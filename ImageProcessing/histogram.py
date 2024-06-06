import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/messi1.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_img_eqhist=cv.equalizeHist(gray_img)

#equ = cv.equalizeHist(img)
#res = np.hstack((img,equ))
#cv.imwrite('res.png',res)
plt.subplot(121), plt.plot(cv.calcHist(gray_img, [0], None, [256], [0, 256])), plt.title("Image Hist")
plt.xlabel('bins'), plt.ylabel("No of pixels")
plt.subplot(122), plt.imshow(gray_img), plt.title("Image")
plt.xticks([]), plt.yticks([])
plt.subplot(221), plt.plot(cv.calcHist(gray_img_eqhist, [0], None, [256], [0, 256])), plt.title("Eq Image Hist")
plt.xlabel('bins'), plt.ylabel("No of pixels")
plt.subplot(222), plt.imshow(gray_img_eqhist), plt.title("Image EQ")
plt.xticks([]), plt.yticks([])

plt.show()