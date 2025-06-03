from cv2 import Canny, imread,cvtColor, COLOR_BGR2GRAY, imshow, IMREAD_COLOR, waitKey, destroyAllWindows, imdecode
from requests import get # to get the image from the URL and store it in bytes
import numpy as np # to convert the bytes to numbers as OpenCV requires a number
from PIL import Image # to open and show the images
import io # to convert the bytes to an image

def bytes_to_image(byte_data):
    try:
        image = Image.open(io.BytesIO(byte_data)) # Open the image from bytes
        print(image)
        image_array = np.frombuffer(byte_data, np.uint8)
        print(image_array)
        img = imdecode(image_array, IMREAD_COLOR) # Decode the image from the byte array
        gray = cvtColor(img, COLOR_BGR2GRAY) # convert to gray color to detect edges
        edges = Canny(gray, 100, 0) # detect edges in the image
        imshow('pokemon', edges) # display the image with edges
        waitKey(0) # Wait for a key press to close the window
        # image.show()  # Display the image

    except Exception as e:
        print(f"Error decoding image: {e}")

r = get('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png')

if r.status_code == 200:
    bytes_to_image(r.content)
else:
    print("Failed to fetch image.")
# print(type(r))
# print(dir(r))
# print(r.apparent_encoding)
# print(r.content)
# print(type(r.content))