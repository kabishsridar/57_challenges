import numpy as np
import cv2 as cv

img = cv.imread('opencv_tutorial\\messi5.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[100,100]
print( px )

img[100,100] = [255,255,255]  # changing pixel value to white
px = img[100,100]
print( px )

print(img.shape)  # shape of the image (height, width, channels)
print(img.size)   # total number of pixels (height * width * channels)
print(img.dtype)  # data type of the pixel values

# accessing only red pixel
red = img[100,100,2]
print( red )

# accessing only blue pixel
blue = img[100,100,0]
print( blue )

b = img[:,:,0]        # all blue pixels
img[:,:,0] = 0        # setting all blue pixels to 0
# img[:,:,2] = 0      # optionally setting all red pixels to 0

mode = True  # if True, draw rectangle. Press 'm' to toggle to circle
drawing = False  # true if mouse is pressed
ix, iy = -1, -1

def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix-50, iy-50), (ix+50, iy+50), (0, 255, 0), 2)
        else:
            cv.circle(img, (x, y), 50, (255, 0, 0), -1)

cv.namedWindow('image')
cv.setMouseCallback('image', draw_shape)

while True:
    cv.imshow('image', img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break
    elif key == ord('m'):
        mode = not mode  # toggle mode

cv.destroyAllWindows()
