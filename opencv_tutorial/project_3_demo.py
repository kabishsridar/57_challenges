import cv2
import numpy as np

# Capture frame
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if not ret:
    print("The frame is not read")
    exit()

# Convert to grayscale and detect edges
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 800)

# Detect lines
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

line_img = frame.copy()
vertical_lines = []

# Filter vertical lines based on x-difference and y-difference
if lines is not None:
    print(len(lines))
    for line in lines:
        x1, y1, x2, y2 = line[0]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx < 10 and dy > 50:  # Rough vertical line check
            x_avg = (x1 + x2) // 2
            vertical_lines.append((x_avg, (x1, y1, x2, y2)))

    # Sort vertical lines by average x position
    vertical_lines.sort(key=lambda l: l[0])

    if len(vertical_lines) >= 3:
        # Get second and third vertical lines
        _, line2 = vertical_lines[1]
        _, line3 = vertical_lines[2]

        # Draw and label them
        for idx, (x_avg, (x1, y1, x2, y2)) in enumerate([vertical_lines[1], vertical_lines[2]], start=2):
            cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            mid_y = (y1 + y2) // 2
            cv2.putText(line_img, f"Line {idx}", (x_avg + 10, mid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Calculate horizontal distance between the second and third lines
        distance = abs(vertical_lines[2][0] - vertical_lines[1][0])
        print(f"Horizontal distance between line 2 and 3: {distance} pixels")
    else:
        print("Less than 3 vertical lines detected.")
else:
    print("No lines detected.")

# Show result
cv2.imshow("Vertical Lines (2nd and 3rd)", line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
