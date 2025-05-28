import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape

# M = np.float32([[1,0,100],[0,1,50]])
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)  # rotate image by 90 degrees around its center1
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()