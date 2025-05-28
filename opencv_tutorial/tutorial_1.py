import cv2 as cv
import sys
# if it is in the same directory, we can use the below line
# img = cv.imread(cv.samples.findFile("rolls.jpg"))
# if it is not in the same directory, we can use the below line
# img = cv.IMREAD_COLOR(("C:\\Users\\OMAC\\Pictures\\New folder\\rolls.jpg"))
# this will work if the image is in the same directory as this script
img = cv.imread("rolls.jpg")
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("q"):
    cv.imwrite("rolls_royce.png", img)
    sys.exit("Image saved as rolls_royce.png and exiting.")
'''
import cv2 as cv
import sys

# Load the image
img = cv.imread("C:\\Users\\OMAC\\Pictures\\New folder\\rolls.jpg")

# Check if the image was loaded
if img is None:
    sys.exit("Could not read the image.")

# Show the image
cv.imshow("Display window", img)

# Loop until 'q' is pressed
while True:
    k = cv.waitKey(0)
    if k == ord("q"):
        cv.imwrite("rolls_royce.png", img)
        print("Image saved as rolls_royce.png")
        break  # exit the loop

# Clean up windows after exiting
cv.destroyAllWindows()
'''