from keras.layers import Dense, Conv2D, Flatten
from keras.utils import to_categorical
from keras.models import Sequential
from keras.datasets import mnist


class ConvNet:
    def __init__(self, train, test):
        self.model = Sequential()
        self.x_train = train[0]
        self.y_train = train[1]

        self.x_test = to_categorical(test[0])
        self.y_test = to_categorical(test[1])

        self.reshaping()

        self.training_metadata = None

    def reshaping(self):
        self.x_train, self.x_test = \
            self.x_train.reshape(self.x_train.shape.__add__((1,))), \
            self.x_test.reshape(self.x_test.shape.__add__((1,)))

    def building_model(self):
        self.model.add(Conv2D(64, kernel_size=3, activation='relu',
                              input_shape=self.x_train.shape))
        self.model.add(Conv2D(32, kernel_size=3, activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(10, activation='softmax'))

    def compiling(self, optmizer='sgd', loss='categorical_crossentropy',
                  metrics=('accuracy',)):
        self.model.compile(optmizer=optmizer, loss=loss, metrics=metrics)

    def training(self):
        return self.model.fit(self.x_train, self.y_train,
                              validation_data=(self.x_test, self.y_test),
                              epochs=3)

    def saving_weights(self, filepath):
        self.model.save_weights(filepath)


if __name__ == '__main__':
    train, test = mnist.load_data()
    ConvNet(train, test)
