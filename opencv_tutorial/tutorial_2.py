import numpy as np
import cv2 as cv
 
# cap = cv.VideoCapture(-1) # Use 0 for the default camera, or -1 for the first available camera
cap = cv.VideoCapture(0) # Use 0 for the default camera, or -1 for the first available camera
if not cap.isOpened():
    # if it is not opened, we can open it using cap.open(), but here we are checking if it is opened
    # and if it is not opened, we will exit the program
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read() # returns a bool (True/False). If the frame is read correctly, it will be True.
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # rgb_image = cv.cvtColor(frame, cv.COLOR_GRAY2RGB)
    # rgb_frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    cv.imshow('Webcam - Original Color', frame)

    # Display the resulting frame
    # cv.imshow('frame', gray)
    # cv.imshow('frame', rgb_image)
    # cv.imshow('frame', rgb_frame)
    if cv.waitKey(1) == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()