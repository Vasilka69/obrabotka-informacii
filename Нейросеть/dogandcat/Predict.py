from tensorflow import keras
import cv2
import numpy as np
import os
from os.path import isfile

predictfile='ImageToPredict\\test.jpg'

path = 'test/'
files = os.listdir(path=path)

for file in files:
    if isfile(path + file):
        print(path + file)
        img = cv2.imread(path + file)
        img = cv2.resize(img, (64, 64))
        img = np.reshape(img, [64, 64, 3])
        cv2.imwrite('ImageToPredict\\test.jpg', img)
        #cv2.imwrite('ImageToPredict\\' + file, img)

model = keras.models.load_model('DogCat.h5')

img = cv2.imread(predictfile)
print(predictfile)
img = cv2.resize(img, (64, 64))
img = np.reshape(img, [1, 64, 64, 3])

prediction = model.predict(img)

if prediction == 0:
    print('Кот')
else:
    print('Собака')