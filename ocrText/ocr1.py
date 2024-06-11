import numpy as np
import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
img = cv.imread("/Users/arhan.sheth/Documents/Codes/DX/Basics/dx_opencvInitial/ocrText/ocrYellowTest.jpeg")
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, th = cv.threshold(grayImg, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
rectKernel = cv.getStructuringElement(cv.MORPH_RECT, (18, 18))
dilation = cv.dilate(th, rectKernel, iterations = 1)
contours, heirarchy = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

img2 = img.copy()

file = open("recognizedText.txt", "w+")
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    rect = cv.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropping = img2[y:y+h, x:x+w]

    file = open("recognizedText.txt", "a")
    text = pytesseract.image_to_string(cropping)

    file.write(f"{text}\n")
    print("Done")
    file.close
