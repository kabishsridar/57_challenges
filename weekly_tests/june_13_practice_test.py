import cv2 as cv # importing the modules
from sys import argv

def face_detection(filename): # defining a function to display the etected faces with rectangle
    img = cv.imread(f'{filename}') # reads the image from the command prompt
    if img is None: # if the image is not found, returns error message
        return "Cannot open image"
        
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converting to gray scale , so that detecting faces is easy

    haar_cascade = cv.CascadeClassifier(r'haar_face.xml') # using the file haar_face.xml to train about faces and stores them as haar_cascade
    if haar_cascade.empty(): # if the file is empty, returns the message and exits
        print("Haar cascade file is empty")
        exit()
    resized = rescaleframe(img) # resizing the images, as some images dimensions are larger than the screen's dimensions
    faces_rect = haar_cascade.detectMultiScale(resized, scaleFactor=1.1, minNeighbors=4) # detects faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), thickness=4) # draws a rectangle on the faces detected

    cv.imshow('detected face', resized) # displaing the detected faces with green rectangle

    cv.waitKey(0) # the file waits to close upto infinite time upto we enter esc
    cv.destroyAllWindows() # destroying all windows

def rescaleframe(frame, max_width=1080, max_height=720):  # You can adjust max screen size if needed
    shape = frame.shape # getting the pixels
    height = shape[0] # dimension of height is first
    width = shape[1] # dimension of width is second

    if width > max_width or height > max_height: # if the image is larger than the screen
        scale_w = max_width / width
        scale_h = max_height / height
        scale = min(scale_w, scale_h)

        new_dimensions = (int(width * scale), int(height * scale)) # shrinken the image
        return cv.resize(frame, new_dimensions, interpolation=cv.INTER_AREA)
    else:
        return frame

if __name__ == "__main__": # using if __name__ condition to run the block first on starting the script
    print(f"script: {argv[0]}")
    print(f"File name: {argv[1]}")
    face_detection(argv[1]) # calling the function with the file name entered in command prompt as "python june_13_practice_test.py {filename}"