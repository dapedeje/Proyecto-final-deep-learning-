import tensorflow as tf
from keras.models import Sequential
from tensorflow.keras import layers, models
from keras.optimizers import Adam

def ModeloComplejo(input_shape, num_clases):
    """
    Esta función permite crear una arquitectura más compleja que la entrega 
    anterior


    Args:
        input_shape (_type_): Tamaño de la entrada
        num_clases (_type_): numero de clases a predecir

    Returns:
        _type_: modelo de keras
    """

    model = Sequential()

    model.add(layers.Conv2D(16, 3, padding='same', input_shape=input_shape))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())
    model.add(layers.Dropout(0.3))
    
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.UpSampling2D((2,2)))   # restore resolution
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(32, 3, padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Dropout(0.3))

    model.add(layers.Flatten())
    model.add(layers.Dense(128))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(num_clases, activation='softmax'))
    
    optimizer_adam = Adam(0.000002)
    model.compile(optimizer=optimizer_adam, loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
    
    return model
