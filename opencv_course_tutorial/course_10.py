import cv2 as cv
import numpy as np

img = cv.imread('opencv_tutorial\\rolls.jps')
cv.imshow('rolls',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 + 45), 100,255, -1)
cv.imshow('Mask', mask)

circle = cv.circle(blank.copy(), (30,30), (370,370), 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('weird shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked', masked)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image',masked)
cv.waitKey(0)