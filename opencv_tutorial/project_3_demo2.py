import cv2
import numpy as np

# List to store clicked points
clicked_points = []

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global clicked_points, image_copy
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        # Draw a vertical line at the clicked point
        cv2.line(image_copy, (x, 0), (x, image_copy.shape[0]), (0, 255, 0), 2)
        # Label the point
        cv2.putText(image_copy, f"{len(clicked_points)}", (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.imshow("Click on 2 vertical lines", image_copy)

        if len(clicked_points) == 2:
            # Calculate horizontal distance
            x1, _ = clicked_points[0]
            x2, _ = clicked_points[1]
            pixel_distance = abs(x2 - x1)
            print(f"Horizontal distance between points: {pixel_distance} pixels")

# Capture one frame from webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if not ret:
    print("Failed to capture image")
    exit()

# Clone frame to draw on
image_copy = frame.copy()

# Create window and set mouse callback
cv2.imshow("Click on 2 vertical lines", image_copy)
cv2.setMouseCallback("Click on 2 vertical lines", mouse_callback)

print("Click on TWO vertical lines in the image to measure their horizontal distance.")
cv2.waitKey(0)
cv2.destroyAllWindows()
