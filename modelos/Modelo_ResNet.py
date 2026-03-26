import tensorflow as tf
from keras.models import Sequential
from tensorflow.keras import layers, models
from keras.optimizers import Adam
from tensorflow.keras.applications import ResNet50
from keras.layers import GlobalAveragePooling2D, Dense
from keras import Model

def Modelo_transfer(input_shape, num_clases):
    """
    Esta función permite crear una arquitectura más compleja que la entrega 
    anterior


    Args:
        input_shape (_type_): Tamaño de la entrada
        num_clases (_type_): numero de clases a predecir

    Returns:
        _type_: modelo de keras
    """
    base_model = ResNet50(weights="imagenet", include_top=False)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256,activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    predictions = Dense(num_clases, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    
    #for layer in base_model.layers:
    #    layer.trainable = False


    optimizer_adam = Adam()
    model.compile(optimizer=optimizer_adam, loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
    
    return model
