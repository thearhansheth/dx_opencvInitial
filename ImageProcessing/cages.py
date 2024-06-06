import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/cages.png", cv.IMREAD_GRAYSCALE)
template = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/whiteCages.png", cv.IMREAD_GRAYSCALE)
template2 = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/blackCages.png", cv.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]
w2, h2 = template2.shape[::-1]
 
res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
res2 = cv.matchTemplate(img, template2, cv.TM_CCOEFF_NORMED)
threshold = 0.88
loc = np.where( res > threshold)
loc2 = np.where(res2 > threshold)

countW = 0
countB = 0
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
    countW+=1
for pt in zip(*loc2[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
    countB+=1

cv.putText(img, f"Black Count is {countB}", (1500, 1500), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
cv.putText(img, f"White Count is {countW}", (1600, 1600), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()