import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('rolls.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# blur = cv.blur(img,(5,5))
# blur = cv.GaussianBlur(img, (5, 5), 0)
# blur = cv.medianBlur(img, 5)
blur = cv.bilateralFilter(img, 9, 75, 75)
# kernel = np.ones((5,5),np.float32)/25
# dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.subplot(122),plt.imshow(blur),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()