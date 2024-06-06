import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/cylinder_test.png")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_img_eqhist=cv.equalizeHist(gray_img)
#Gaus blur

#equ = cv.equalizeHist(img)
#res = np.hstack((img,equ))
#cv.imwrite('res.png',res)
#plt.subplot(121), plt.plot(cv.calcHist(gray_img, [0], None, [256], [0, 256])), plt.title("Image Hist")
#plt.xlabel('bins'), plt.ylabel("No of pixels")
plt.subplot(121), plt.imshow(cv.cvtColor(gray_img, cv.COLOR_GRAY2RGB)), plt.title("Image")
plt.xticks([]), plt.yticks([])
#plt.subplot(221), plt.plot(cv.calcHist(gray_img_eqhist, [0], None, [256], [0, 256])), plt.title("Eq Image Hist")
#plt.xlabel('bins'), plt.ylabel("No of pixels")
plt.subplot(122), plt.imshow(cv.cvtColor(gray_img_eqhist, cv.COLOR_GRAY2RGB)), plt.title("Image EQ")
plt.xticks([]), plt.yticks([])
eqhist_images = np.concatenate((gray_img, gray_img_eqhist), axis = 1)
cv.imwrite("eqhist_images.png", eqhist_images)

plt.show()
