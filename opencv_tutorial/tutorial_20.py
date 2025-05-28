import cv2 as cv
import numpy as np

img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow('Tophat', tophat)
cv.imshow('Blackhat', blackhat)
cv.imshow('Gradient', gradient)
cv.imshow('Opening', opening)
cv.imshow('Closing', closing)
cv.imshow('Dilation', dilation)
cv.imshow('Erosion', erosion)
cv.imshow('Original', img)
cv.waitKey(0)
cv.destroyAllWindows()