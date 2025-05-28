import cv2 as cv
import numpy as np

# OBject detection using color in OpenCV
# This code captures video from the webcam and detects blue color in the frames.
cap = cv.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV to detect
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    # pixels within the range of blue will be white, others will be black
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame) # original image
    cv.imshow('mask',mask) # mask image
    cv.imshow('res',res) # result image
    k = cv.waitKey(5) & 0xFF # this will exit with esc key
    if k == 27:
        break

cv.destroyAllWindows()