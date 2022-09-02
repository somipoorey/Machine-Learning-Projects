from flask import Flask,render_template, request
import tensorflow as tf
from keras.utils import img_to_array
import numpy as np
import cv2
import os
from keras.models import load_model


app = Flask(__name__)
model = load_model("./saved_model/1")
classes = ['Male','Female']

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    image = cv2.imread(image_path)
    image = cv2.resize(image, (96,96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    yhat =  model.predict(image)
    ypred = np.argmax(yhat)

    return render_template('index.html', prediction=ypred)

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)