import cv2 as cv
import numpy as np

img = cv.imread('opencv_tutorial\\rolls.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)
ret, thresh = cv. threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('THRESH', thresh)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny edges', canny)

contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour found")

cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow('contours drawn', blank)

cv.waitKey(0)