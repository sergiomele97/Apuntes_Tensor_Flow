import tensorflow as tf
import numpy as np


np.set_printoptions(precision=3, suppress=True)     # setting up numpy display


training_data = np.load("training_data.npy")
training_labels = np.load("training_labels.npy")
testing_data = np.load("testing_data.npy")
testing_labels = np.load("testing_labels.npy")



print(training_data.shape)

model = tf.keras.models.Sequential([tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(5, activation=tf.nn.softmax)])


model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(training_data, training_labels, epochs=20)

model.summary()

model.evaluate(testing_data, testing_labels)
