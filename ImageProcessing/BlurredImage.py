import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/blured_test.png")
wntImg = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/blurred_result.png")

sharpenKernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#Maybe other kernels?
unblurImg = cv.filter2D(img, -1, sharpenKernel)
blurringImg = cv.blur(wntImg, (5, 5))

plt.subplot(141), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Blurred")
plt.xticks([]), plt.yticks([])
plt.subplot(142), plt.imshow(cv.cvtColor(unblurImg, cv.COLOR_BGR2RGB)), plt.title("UnBlurred")
plt.xticks([]), plt.yticks([])
plt.subplot(143), plt.imshow(cv.cvtColor(wntImg, cv.COLOR_BGR2RGB)), plt.title("Wanted Final")
plt.xticks([]), plt.yticks([])
#plt.subplot(144), plt.imshow(cv.cvtColor(blurringImg, cv.COLOR_BGR2RGB)), plt.title("Blurred Final")
#plt.xticks([]), plt.yticks([])
plt.show()

combinedImages = np.concatenate((img, unblurImg), axis = 1)
cv.imwrite("blurImageQues.png", combinedImages)