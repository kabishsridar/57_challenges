from cv2 import imshow, destroyAllWindows, addWeighted, waitKey, setMouseCallback, namedWindow, imread, VideoCapture, circle, EVENT_LBUTTONUP, EVENT_LBUTTONDOWN, EVENT_MOUSEMOVE
import numpy as np

cap = VideoCapture(0)
ret, frame = cap.read()
ix , iy = -1, -1
drawing = False
frame2 = frame.copy()
if not ret:
    print("Frame cannot be read")
def coordinates(event, x, y, flags, param):
    global ix, iy, drawing
    if event == EVENT_LBUTTONDOWN:
        ix, iy = x, y
        drawing = True
        print(f"x:{x}, y:{y}")
    elif event == EVENT_MOUSEMOVE:
        if drawing == True:
            circle(frame, (x, y), 5, (0,255,0), -1)
            print(f"x:{x}, y:{y}")
    elif event == EVENT_LBUTTONUP:
        drawing = False
        circle(frame, (x,y), 10, (0, 255,0), 1)

#imshow('webcam', frame)
namedWindow('webcam Doodle')
setMouseCallback('webcam Doodle', coordinates)
while(1):
    merged = frame.copy()
    merged = addWeighted(merged,1, frame2,1,0)
    imshow('webcam Doodle', frame)
    if waitKey(1) == ord('q'):
        break
cap.release()
destroyAllWindows()