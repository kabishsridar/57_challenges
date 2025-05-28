import cv2 as cv
import numpy as np

window = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('window', window)

window[200:300, 300:400] = 0,0,255
# cv.imshow('red', window)

cv.rectangle(window, (0,0), (250,250), (0,255,0), thickness=-1)
# cv.rectangle(window, (0,0), (window.shape[1]//2), window.shape([0]//2), (0, 255,0), thickness=1)

cv.putText(window, 'Hello', (255,255), cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)

cv.imshow('rect', window)

cv.waitKey(0)