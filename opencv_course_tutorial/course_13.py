import cv2 as cv

# Load image
img = cv.imread('opencv_course_tutorial\\vijay.jpg')

# Validate image loading
if img is None:
    print("Error: Image not found. Check the path!")
    exit()

cv.imshow('vijay', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)  # Fixed typo in window name

# Load Haar Cascade
haar_cascade = cv.CascadeClassifier(r'C:\\kabish_python\\57_challenges\\opencv_course_tutorial\\haar_face.xml')

# Validate Haar Cascade loading
if haar_cascade.empty():
    print("Error: Haar Cascade XML file not found. Check the path!")
    exit()

# Detect faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f"Number of faces found = {len(faces_rect)}")

# Draw rectangles around detected faces
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected', img)

cv.waitKey(0)
cv.destroyAllWindows()  # Ensure all windows close properly