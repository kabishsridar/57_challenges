import numpy as np
import cv2 as cv

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),50,(255,100,0),-1) # 50 is the radius, (255,200,0) is the color in BGR format, -1 means filled circle

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(1) == ord("q"):
        break
cv.destroyAllWindows()