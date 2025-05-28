import cv2 as cv
import numpy as np

img = cv.imread('opencv_tutorial\\rolls.jpg')
cv.imshow('rolls', img)

average = cv.blur(img, (3,3))
cv.imshow('Average', average)

guass = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Guassian', guass)

median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)
cv.waitkey(0)