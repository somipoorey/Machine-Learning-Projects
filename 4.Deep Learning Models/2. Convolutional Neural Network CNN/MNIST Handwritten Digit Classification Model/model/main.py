from flask import Flask,render_template, request
import tensorflow as tf
from keras.utils import img_to_array
import numpy as np
import cv2
import os
from keras.models import load_model


app = Flask(__name__)
model = load_model("./saved_model/MNIST")
classes = [0,1,2,3,4,5,6,7,8,9]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    if request.files['imagefile'].filename != "":

        imagefile = request.files['imagefile']
        image_path = "./images/" + imagefile.filename
        imagefile.save(image_path)

        image = cv2.imread(image_path,0)
        image = cv2.resize(image, (28,28))
        image = image.reshape(1,28,28,1)
        image = image.astype("float") / 255.0
        
        yhat =  model.predict(image)
        ypred = np.argmax(yhat)

        return render_template('index.html', prediction=ypred)
    else:
        return render_template('index.html',prediction="empty")

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)