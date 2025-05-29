from cv2 import imshow, destroyAllWindows, addWeighted,putText, FONT_HERSHEY_SIMPLEX, LINE_AA, waitKey, setMouseCallback, namedWindow, imread, VideoCapture, circle, EVENT_LBUTTONUP, EVENT_LBUTTONDOWN, EVENT_MOUSEMOVE
import numpy as np

cap = VideoCapture(0)
ret, frame = cap.read()
ix , iy = -1, -1
drawing = False
frame2 = frame.copy()
x1 = x2 = y1 = y2 = -1
distance_cm = None

if not ret:
    print("Frame cannot be read")
# 1cm = 21 px

def coordinates(event, x, y, flags, param):
    global ix, iy, drawing, x1, y1, x2, y2, frame

    if event == EVENT_LBUTTONDOWN:
        ix, iy = x, y
        drawing = True
        x1, y1 = x, y
        print(f"Start Point - x:{x}, y:{y}")
    
    elif event == EVENT_MOUSEMOVE and drawing:
        circle(frame, (x, y), 10, (0, 255, 0), -1)
    
    elif event == EVENT_LBUTTONUP:
        drawing = False
        x2, y2 = x, y
        circle(frame, (x, y), 10, (0, 255, 0), 1)
        print(f"End Point - x:{x}, y:{y}")
        convert_px_to_cm()

def convert_px_to_cm():
    global x1, y1, x2, y2, distance_cm
    if x1 != -1 and x2 != -1:
        px1 = x2 - x1
        px2 = y2 - y1
        cm1 = px1 / 21
        cm2 = px2 / 21
        distance_cm = (cm1**2 + cm2**2)**0.5
        print(f"Distance: {distance_cm:.2f} cm")
#imshow('webcam', frame)
namedWindow('webcam Doodle')
setMouseCallback('webcam Doodle', coordinates)
while(1):
    merged = frame.copy()
    merged = addWeighted(merged,1, frame2,1,0)
    ret, frame = cap.read()
    if not ret:
        break
    if distance_cm is not None:
        putText(frame, f"Distance: {distance_cm} cm", (40, 450), FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, LINE_AA)

    imshow('webcam Doodle', frame)
    if waitKey(1) == ord('q'):
        break

cap.release()
destroyAllWindows()