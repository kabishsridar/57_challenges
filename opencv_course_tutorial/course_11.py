import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('opencv_tutorial\\rolls.jpg')
cv.imshow('rolls', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)