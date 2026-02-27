import tensorflow as tf
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, BatchNormalization, Dropout, MaxPooling2D,GlobalAveragePooling2D
from keras import regularizers
from keras.optimizers import Adam
from keras.layers import ReLU

def ModeloSimpleCLS(input_shape, num_clases):
    """
    Esta función permite cargar una arquitectura simple para un modelo CNN.

    Args:
        input_shape (_type_): Insertar el tamaño de la entrada para el modelo
    """
    model = Sequential()
    
    model.add(Conv2D(32, kernel_size= 3, activation='relu', input_shape=(32,32,3)))
    model.add(Flatten())
    model.add(Dense(num_clases, activation='softmax'))
    
    optimizer_adam = Adam()
    model.compile(optimizer=optimizer_adam, loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    
    return model