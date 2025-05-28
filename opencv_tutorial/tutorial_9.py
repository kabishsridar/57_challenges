import cv2 as cv
import numpy as np                              

img1 = cv.imread('rolls_royce.png')
img2 = cv.imread('messi.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

dst = cv.addWeighted(img1,0.7,img2,0.3,0) # blending images
# dst = cv.add(img1,img2)  # adding images
# dst = cv.subtract(img1,img2)  # subtracting images

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()