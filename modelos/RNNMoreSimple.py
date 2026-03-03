import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, GlobalAveragePooling2D
from keras.optimizers import Adam

def ModeloSimpleCLS(input_shape, num_clases):
    """
    Esta función permite cargar una arquitectura simple para un modelo CNN.

    Args:
        input_shape (_type_): Insertar el tamaño de la entrada para el modelo
    """
    model = Sequential()
    
    model.add(Conv2D(num_clases, kernel_size= 3, activation='relu', input_shape=input_shape))
    model.add(GlobalAveragePooling2D())

    model.compile(
        optimizer=Adam(),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['sparse_categorical_accuracy']
    )
    
    return model
