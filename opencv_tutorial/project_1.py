import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

ix, iy = -1, -1
drawing = False  # True if mouse is pressed

if not cap.isOpened():
    print("Cannot open camera")
    exit()
ret, frame = cap.read()
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    exit()
# Mouse callback function for doodling on the webcam feed
def doodle_webcam(event, x, y, flags, param):
    global drawing, ix, iy
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(frame, (x, y), 10, (0, 255, 0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(frame, (x, y), 10, (0, 255, 0), -1)
cv.imshow('Webcam Doodle', frame)
cv.namedWindow('Webcam Doodle')
cv.setMouseCallback('Webcam Doodle', doodle_webcam)
print(ord('q'))
while(1):
    cv.imshow('Webcam Doodle', frame)
    if cv.waitKey(1) == ord('q'):
        # print("Breaked")
        break
    # print(ord('q'))
    # print(cv.waitKey(1))
    if cv.waitKey(1) == ord('a'):
        cv.imwrite("project1.png", frame)
        print("I am inside the writing")
        break
cap.release()
cv.destroyAllWindows()