import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout
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
    
    model.add(Conv2D(32, kernel_size= 3, activation='relu', input_shape=input_shape))
    model.add(Dropout(0.2))
    
    model.add(Conv2D(64, 3, activation= 'relu')) #Añadimos complejidad
    model.add(Dropout(0.2))
    
    model.add(Flatten())
    model.add(Dense(64, activation= 'relu'))#Añadimos complejidad
    model.add(Dropout(0.2))
    model.add(Dense(num_clases, activation='softmax'))#Añadimos complejidad
    
    optimizer_adam = Adam()
    model.compile(optimizer=optimizer_adam, loss='sparse_categorical_crossentropy', metrics=['categorical_accuracy'])
    
    return model
