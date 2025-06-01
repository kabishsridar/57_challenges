import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("the frame is not read")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 800)
cv2.imshow("Edges", edges)
print(f"{edges.ndim}")
print(type(edges))
""" while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 800)
    cv2.imshow("Edges", edges)
    print(edges)
    print(type(edges))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break """
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)
""" # Show edges
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows() """
line_img = frame.copy()

# Draw lines (if any detected)
if lines is not None:
    print(len(lines))
    for i, line in enumerate(lines):
        x1, y1, x2, y2 = line[0]
        print(x1)
        cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        cv2.putText(line_img, f"#{i+1}", (mid_x, mid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
# Show images
cv2.imshow("Original Frame with Lines", line_img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
# If no lines are detected
if lines is None or len(lines) < 2:
    print("Not enough lines detected to calculate distance.")
    exit()

# Extract first two lines (x1, y1, x2, y2)
x1_1, y1_1, x2_1, y2_1 = lines[0][0]
x1_2, y1_2, x2_2, y2_2 = lines[1][0]

# Convert first line to a vector and point
line1_vector = np.array([x2_1 - x1_1, y2_1 - y1_1])
point_on_line1 = np.array([x1_1, y1_1])
point_on_line2 = np.array([x1_2, y1_2])  # We'll use a point from line 2

# Calculate the distance from point_on_line2 to line1
numerator = np.abs(np.cross(line1_vector, point_on_line2 - point_on_line1))
denominator = np.linalg.norm(line1_vector)
distance = numerator / denominator

print(f"Distance between line 1 and line 2: {distance:.2f} pixels")

cap.release()
cv2.destroyAllWindows()