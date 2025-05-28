import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3) # Draw a rectangle
cv.circle(img,(447,63), 63, (0,0,255), -1) # Draw a filled circle
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1) # Draw a filled ellipse
cv.putText(img,'Hello kabish',(150,500), cv.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv.LINE_AA) # Add text

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32) # Create a polygon
pts = pts.reshape((-1,1,2)) # Reshape the points
cv.polylines(img,[pts],True,(0,255,255),3) # Draw the polygon

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,250), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()