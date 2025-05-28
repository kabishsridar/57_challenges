import cv2 as cv
import numpy as np

img = cv.imread('opencv_tutorial\\rolls.jpg')

cv.imshow('rolls royce', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[1])
    return cv.warpAffine(img, transMat, dimension)

def rotated(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated_img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imshow('rotated', rotated_img)

translated = translate(img, 100,100)
cv.imshow('translated', translated)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

flip = cv.flip(img, 1)
cv.imshow('flip',flip)



cv.waitKey(0)