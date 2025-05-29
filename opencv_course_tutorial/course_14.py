import os
import cv2 as cv
import numpy as np

people = ['vijay', 'Elton']
DIR = r'C:\\kabish_python\\57_challenges\\opencv_tutorial'

haar_cascade = cv.CascadeClassifier('C:\\kabish_python\\57_challenges\\opencv_course_tutorial\\haar_face.xml')

# Validate Haar Cascade loading
if haar_cascade.empty():
    print("Error: Haar Cascade XML file not found. Check the path!")
    exit()

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        if not os.path.exists(path):
            print(f"Error: Directory '{path}' not found.")
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Skipping unreadable image: {img_path}")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training done ")

features = np.array(features, dtypes='object')
labels = np.array(labels)
face_recogonizer = cv.face.LBPHFaceRecogonizer_create()

face_recogonizer.train(features, labels)

np.save('features.npy', features)
np.save('labels.npy', labels)