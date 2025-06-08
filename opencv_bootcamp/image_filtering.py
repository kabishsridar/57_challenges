import cv2 # importing the libraries
import sys
import numpy

PREVIEW  = 0  # Preview Mode
BLUR     = 1  # Blurring Filter
FEATURES = 2  # Corner Feature Detector
CANNY    = 3  # Canny Edge Detector

feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9) # assigning the variables for corner detection
s = 0
if len(sys.argv) > 1: # checking if the user has provided a file name
    s = sys.argv[1]

image_filter = PREVIEW # setting the default filter to preview and changes for the user input
alive = True

win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s) # opening the camera or video file

while alive:
    has_frame, frame = source.read() # reading the frame from the camera or video file
    if not has_frame:
        break

    frame = cv2.flip(frame, 1) # flipping the frame horizontally for a mirror effect

    if image_filter == PREVIEW: # if it is in preview mode, it will show the original frame
        result = frame
    elif image_filter == CANNY: # if it is in canny mode, it will apply the canny edge detection filter
        result = cv2.Canny(frame, 80, 200)
    elif image_filter == BLUR: # if it is in blur mode, it will apply the blur filter
        result = cv2.blur(frame, (13, 13))
    elif image_filter == FEATURES: # if it is in features mode, it will apply the corner detection filter
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converting the frame to grayscale
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params) # detecting corners
        if corners is not None:
            for x, y in numpy.float32(corners).reshape(-1, 2): 
                cv2.circle(result, (x, y), 10, (0, 255, 0), 1)

    cv2.imshow(win_name, result) # displaying the result in the window

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27: # if the user presses Q or q or ESC, it will exit the loop
        alive = False
    elif key == ord("C") or key == ord("c"): # if the user presses C or c, it will apply the canny edge detection filter
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"): # if the user presses B or b, it will apply the blur filter
        image_filter = BLUR
    elif key == ord("F") or key == ord("f"): # if the user presses F or f, it will apply the corner detection filter
        image_filter = FEATURES
    elif key == ord("P") or key == ord("p"): # if the user presses P or p, it will switch back to preview mode
        image_filter = PREVIEW

source.release() # releasing the camera or video file
cv2.destroyWindow(win_name) # destroying the window