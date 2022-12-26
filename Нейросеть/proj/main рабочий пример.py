import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from tensorflow import keras
#%matplotlib inline
#from tensorflow.keras.datasets import fashion_dataset
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import utils
import tensorflow as tf
import tensorflow_datasets as tfds


def main():
    #dataset = tfds.load('open_images_v4', split='train[10%]')
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    index = 0
    '''
    plt.figure()
    plt.imshow(x_train[index]) # 0 - 59999
    plt.colorbar()
    plt.grid(False)
    '''
    # Нормализуем
    x_train = x_train / 255
    x_test = x_test / 255
    ###
    '''
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(x_train[i], cmap=plt.cm.binary)
        pl.xlabel(class_names[y_train[i]])
    plt.show()
    '''
    # Нейросеть
    path_to_load = 'savedmodel/'

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dense(10, activation="softmax")
    ])

    # Компиляция модели
    model.compile(optimizer=keras.optimizers.SGD(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    # Обучение
    model.fit(x_train, y_train, epochs=10)
    model.save(path_to_load)

    # Проверка точности предсказаний

    test_loss, test_acc = model.evaluate(x_test, y_test)
    print('Test accuracy: ', test_acc)

    # Загрузка модели
    #model = keras.models.load_model(path_to_load)

    # Предсказание
    predictions = model.predict(x_train)
    dictinary = dict(zip(class_names, predictions[index]))
    print(f'Список классов и их вероятности')
    for key in dictinary.keys():
        if dictinary[key] == max(dictinary.values()):
            print('>', end='')
        print(f'{key} : {dictinary[key]}')
    plt.show()


if __name__ == '__main__':
    main()