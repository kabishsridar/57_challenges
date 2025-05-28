import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[100,100]
print( px )

img[100,100] = [255,255,255]  # changing pixel value to white
px = img[100,100]
print( px )

print(img.shape)  # shape of the image (height, width, channels)
print(img.size)  # total number of pixels (height * width * channels)
print(img.dtype)  # data type of the pixel values
# accessing only red pixel
red = img[100,100,2]
print( red )
# accessing only blue pixel
blue = img[100,100,0]
print( blue )
b = img[:,:,0]  # all blue pixels
img[:,:,0] = 0  # setting all blue pixels to 0
# img[:,:,2] = 0  # setting all red pixels to 0

mode = True  # if True, draw rectangle. Press 'm' to toggle to circle
drqawing = False  # true if mouse is pressed
ix, iy = -1, -1

def draw_rectangle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x-50, y-50), (x+50, y+50), (0, 255, 0), 2)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_rectangle)
while True:
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == 27:  # exit on ESC key
        break
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 50, (255, 0, 0), -1)  # filled circle with radius 50
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while True:
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == 27:  # exit on ESC key
        break
                    
cv.destroyAllWindows()