from tensorflow import keras
from keras import layers, Model
DICT = {'50': [3, 4, 6, 3], '101': [3, 4, 23, 3], 152: [3, 8, 36, 3]}

DICT = {'50': [1, 2, 2, 1], '101': [3, 4, 23, 3], 152: [3, 8, 36, 3]}
KERNEL_SHAPE = (3, 3)
SHAPE = (224, 224, 1)
CLASS = 100

FIRST_LAYER_FILTER_SIZE = [64, 64, 256]
SECOND_LAYER_FILTER_SIZE = [128, 128, 512]
THIRD_LAYER_FILTER_SIZE = [256, 256, 1024]
FORTH_LAYER_FILTER_SIZE = [512, 512, 2048]


def conv_block(initial_x, FILTER_SIZE):
    # 1st layer
    x = layers.Conv2D(FILTER_SIZE[0], 1)(initial_x)
    x = layers.BatchNormalization(axis=1)(x)
    x = layers.Activation('relu')(x)

    # 2nd layer
    x = layers.Conv2D(FILTER_SIZE[1],
                      KERNEL_SHAPE, padding='same')(x)
    x = layers.BatchNormalization(axis=1)(x)
    x = layers.Activation('relu')(x)

    # 3rd layer
    x = layers.Conv2D(FILTER_SIZE[2], 1)(x)
    x = layers.BatchNormalization(axis=1)(x)

    initial_x = layers.Conv2D(FILTER_SIZE[2],
                              KERNEL_SHAPE)(initial_x)
    initial_x = layers.BatchNormalization(axis=1)(initial_x)
    x = layers.add([x, initial_x])
    x = layers.Activation('relu')(x)

    return x


def identity_block(initial_x, SECOND_LAYER_FILTER_SIZE):
    # 1st layer
    x = layers.Conv2D(SECOND_LAYER_FILTER_SIZE[0], 1)(initial_x)
    x = layers.BatchNormalization(axis=1)(x)
    x = layers.Activation('relu')(x)

    # 2nd layer
    x = layers.Conv2D(SECOND_LAYER_FILTER_SIZE[1],
                      KERNEL_SHAPE,
                      padding='same')(x)
    x = layers.BatchNormalization(axis=1)(x)
    x = layers.Activation('relu')(x)

    # 3rd layer
    x = layers.Conv2D(SECOND_LAYER_FILTER_SIZE[2], 1)(x)
    x = layers.BatchNormalization(axis=1)(x)
    x = layers.add([x, initial_x])
    x = layers.Activation('relu')(x)

    return x


def get_resnet_Model(model_input,
                     FIRST_LAYER_FILTER_SIZE,
                     SECOND_LAYER_FILTER_SIZE,
                     THIRD_LAYER_FILTER_SIZE,
                     FORTH_LAYER_FILTER_SIZE
                     ):

    x = layers.ZeroPadding2D(padding=(3, 3))(model_input)
    x = layers.Conv2D(64, 7, strides=(2, 2))(x)
    x = layers.BatchNormalization(axis=1)(x)
    x = layers.Activation('relu')(x)
    x = layers.ZeroPadding2D(padding=(1, 1))(x)
    x = layers.MaxPooling2D((3, 3), strides=(2, 2))(x)

    # 1st layer
    x = conv_block(x, FIRST_LAYER_FILTER_SIZE)
    x = identity_block(x, FIRST_LAYER_FILTER_SIZE)
    x = identity_block(x, FIRST_LAYER_FILTER_SIZE)

    # 2nd layer
    x = conv_block(x, SECOND_LAYER_FILTER_SIZE)
    x = identity_block(x, SECOND_LAYER_FILTER_SIZE)
    x = identity_block(x, SECOND_LAYER_FILTER_SIZE)
    x = identity_block(x, SECOND_LAYER_FILTER_SIZE)

    # 3rd layer
    x = conv_block(x, THIRD_LAYER_FILTER_SIZE)
    x = identity_block(x, THIRD_LAYER_FILTER_SIZE)
    x = identity_block(x, THIRD_LAYER_FILTER_SIZE)
    x = identity_block(x, THIRD_LAYER_FILTER_SIZE)
    x = identity_block(x, THIRD_LAYER_FILTER_SIZE)
    x = identity_block(x, THIRD_LAYER_FILTER_SIZE)

    # 4th layer
    x = conv_block(x, FORTH_LAYER_FILTER_SIZE)
    x = identity_block(x, FORTH_LAYER_FILTER_SIZE)
    x = identity_block(x, FORTH_LAYER_FILTER_SIZE)

    x = layers.AveragePooling2D((2, 2))(x)

    model_output = layers.Dense(CLASS, activation='softmax')(x)

    model = Model(model_input, model_output)

    return model


if __name__ == '__main__':
    model_size = str(50)  # int(input("Desire ResNet Model Size: "))
    model_input = keras.Input(shape=SHAPE)
    ResNet_Model = get_resnet_Model(model_input,
                                    FIRST_LAYER_FILTER_SIZE,
                                    SECOND_LAYER_FILTER_SIZE,
                                    THIRD_LAYER_FILTER_SIZE,
                                    FORTH_LAYER_FILTER_SIZE)
    ResNet_Model.save("inshaallah.h5")