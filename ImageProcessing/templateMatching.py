import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

mainImg = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/messi1.jpg", cv.IMREAD_GRAYSCALE)
if mainImg is None:
    print("Error")
    exit(1)
img = mainImg.copy()
template = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/messiTemplate.jpeg", cv.IMREAD_GRAYSCALE)
if template is None:
    print("Error")
    exit(1)
widthT, heightT = template.shape[::-1]

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]
methodNames = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR', 'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']

for meth, methName in zip(methods, methodNames):
    mainImg = img.copy()
    method = meth

    # Applying Template Matching
    res = cv.matchTemplate(mainImg, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    # Take minimum if method is TM_SQDIFF or TM_SQDIFF_NORMED
    if meth in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        topLeft = min_loc
    else:
        topLeft = max_loc
    bottomRight = (topLeft[0] + widthT, topLeft[1] + heightT)

    cv.rectangle(img, topLeft, bottomRight, 0, 2)
    plt.subplot(131), plt.imshow(res, cmap = 'gray')
    plt.title("Matching Result")
    plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(img)
    plt.title("Matching Point")
    plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(template)
    plt.title("Template")
    plt.xticks([]), plt.yticks([])
    plt.suptitle(methName)
    plt.show()