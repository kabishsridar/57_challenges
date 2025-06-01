from cv2 import imread, imshow, waitKey, destroyAllWindows
from requests import get
import numpy as np

r = get('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png')
data = r.json()
print(data.keys())
# img = cv.imread('pokemon.png')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# edges = cv.Canny(gray, 100, 0)

# imshow(r)
# imshow('pokemon', edges)

waitKey(0)
destroyAllWindows()