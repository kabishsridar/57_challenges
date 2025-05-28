import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Check camera is working
if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
if not ret:
    print("Can't receive frame (camera issue)")
    cap.release()
    exit()

# Use actual frame size
frame_height, frame_width = frame.shape[:2]
fourcc = cv.VideoWriter_fourcc(*'MJPG')  # Try 'MJPG' if 'XVID' doesn't work
out = cv.VideoWriter('output2.avi', fourcc, 20.0, (frame_width, frame_height))

# Confirm writer works
if not out.isOpened():
    print("Failed to open VideoWriter")
    cap.release()
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    # frame = cv.flip(frame, 0) # this is to flip the video vertically
    out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
