import cv2 as cv
import numpy as np

img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/arhan_ocr_task/images/sample input images/test_rotate.jpg")
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#rows, cols = img.shape
smoothImg = cv.fastNlMeansDenoising(grayimg, h = 10)
T_, thresh = cv.threshold(smoothImg, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)
closingImage = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=5)

edges = cv.Canny(closingImage, 100, 200)
#lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
#for line in lines:
#    x1,y1,x2,y2 = line[0]
#    cv.line(edges,  (x1,y1),  (x2,y2), (0,255,0), 2)
lines = cv.HoughLines(edges,1,np.pi/180,200)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
 
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

#M = cv.getRotationMatrix2D(((cols - 1)/2.0, (rows - 1)/2.0), 5, 1)
#res = cv.warpAffine(img, M, (rows, cols))

#cv.imshow("Result", res)
cv.imshow("Closing", closingImage)
cv.imshow("Result", edges)
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()