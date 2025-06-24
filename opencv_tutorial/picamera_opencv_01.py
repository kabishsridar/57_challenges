# main.py
# This script captures video from the Raspberry Pi camera and displays it in a live preview window.
# It uses the Picamera2 library for camera control and OpenCV for displaying the video feed.

import cv2
from picamera2 import Picamera2
import time
def main():
    """
    Initializes the camera, creates a preview window, and displays the live feed.
    The loop continues until the 'q' key is pressed.
    """
    print("Initializing camera...")
    # Initialize Picamera2
    picam2 = Picamera2()

    # Configure the camera for preview. We create a configuration object.
    # The main stream is configured for a larger resolution, suitable for saving or processing.
    # The lores stream is for a smaller, faster preview. We'll use the main stream for display.
    config = picam2.create_preview_configuration(main={"size": (1280, 720)}, lores={"size": (640, 480)}, display="lores")
    picam2.configure(config)

    # Start the camera. The sensor will now be active.
    picam2.start()

    print("Camera started. Press 'q' in the preview window to exit.")
    
    # Give the camera some time to warm up
    time.sleep(1) 

    # Create a window to display the stream
    cv2.namedWindow("Raspberry Pi Camera Live Preview", cv2.WINDOW_NORMAL)

    try:
        # Loop to continuously capture and display frames
        while True:
            # Capture a frame from the camera. This returns a NumPy array.
            frame = picam2.capture_array()

            # Display the captured frame in the OpenCV window
            cv2.imshow("Raspberry Pi Camera Live Preview", frame)

            # Wait for a key press. If 'q' is pressed, break the loop.
            # cv2.waitKey(1) returns the code of the pressed key or -1 if no key is pressed.
            # The & 0xFF is a bitmask to get the last 8 bits, which is the ASCII value.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("'q' pressed, exiting...")
                break
    finally:
        # Clean up resources
        print("Stopping camera and closing windows.")
        picam2.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

