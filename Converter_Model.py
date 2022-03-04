import tensorflow as tf
from keras.models import load_model

model = load_model('My_Model.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

print("Model Converted Succesfullu")

with open('model.tflite','wb') as f:
    f.write(tflite_model)