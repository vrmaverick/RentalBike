from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
from plot import evaluate

def model(X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=52)
    print(np.array(X_train))
    # Crating a model
    # Names are optional and are used for better visualization of structure below
    mod = tf.keras.Sequential([
        tf.keras.layers.Dense(100,activation="relu",name='input_layer'), # softmax does not work here
        tf.keras.layers.Dense(100,activation="relu",kernel_regularizer='l2'),
        tf.keras.layers.Dense(100,activation="relu"),
        tf.keras.layers.Dense(100,activation="relu"),
        tf.keras.layers.Dense(200,activation="relu"),
        tf.keras.layers.Dense(100,activation="relu",kernel_regularizer='l2'),
        tf.keras.layers.Dense(1,name='output_layer')
    ],name = 'NonLinear')
    mod.compile(loss = tf.keras.losses.mae,
                # optimizer = tf.keras.optimizers.SGD(),
                optimizer = tf.keras.optimizers.Adam(lr=10),
                metrics = ['mae'])
    history = mod.fit(X_train,y_train,epochs=900,verbose=0)
    mod.save("/content/drive/MyDrive/datasets/sales1.h5")
    print(mod.evaluate(X_test,y_test))
    evaluate(history)

