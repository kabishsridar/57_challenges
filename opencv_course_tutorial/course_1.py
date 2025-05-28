import cv2 as cv

# Load image (Uncomment if needed)
# img = cv.imread('opencv_tutorial\\rolls.jpg')
# cv.imshow('rolls royce', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) 
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeres(width, height): # only for live video
    cap.set(3, width)
    cap.set(4, height)
cap = cv.VideoCapture('opencv_tutorial\\output2.avi')

while True:
    isTrue, frame = cap.read()
    
    if not isTrue:
        break
    
    resized_image = rescaleFrame(frame)
    cv.imshow('video', frame)
    cv.imshow('video resized', resized_image)

    if cv.waitKey(1) & 0xFF == ord('q'):  # Changed from `0` to `1` for smooth video playback
        break

cap.release()
cv.destroyAllWindows()