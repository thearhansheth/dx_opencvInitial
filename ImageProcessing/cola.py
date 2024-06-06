import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/cola.jpg", cv.IMREAD_GRAYSCALE)
if img is None:
    print("Error")
    exit(1)
ogImage = img.copy()
template = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/colaTemp.jpg", cv.IMREAD_GRAYSCALE)
if template is None:
    print("Error")
    exit(1)
widthT, heightT = template.shape[::-1]

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]
methodNames = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR', 'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']

for method, methodName in zip(methods, methodNames):
    img = ogImage.copy()
    m = method

    res = cv.matchTemplate(img, template, m)
    minVal,  minLoc, maxVal, maxLoc = cv.minMaxLoc(res)

    if m in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        topLeft = minLoc
    else:
        topLeft = maxLoc
    bottomRight = (topLeft[0] + widthT, topLeft[1] + heightT)

    cv.rectangle(img, topLeft, bottomRight, 0, 2)
    plt.subplot(121), plt.imshow(res)
    plt.title("Matching Result")
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img)
    plt.title("Matching Point")
    plt.xticks([]), plt.yticks([])
    plt.suptitle(methodName)
    plt.show()
"""
_, th = cv.threshold(grayImg, 127, 255, 0)
contours, heirarchy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    cnt = contours[i]
    x, y, w, h = cv.boundingRect(cnt)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.drawContours(img, contours, -1, (0, 255, 0), 2)

cv.imshow("Original Image", ogImage)
cv.imshow("Contoured Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
"""