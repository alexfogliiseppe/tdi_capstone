import os
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard, EarlyStopping
from keras import optimizers
from time import time
from PIL import Image


np.random.seed(123)  # for reproducibility
UPLOAD_FOLDER = 'static/img'


# WEBAPP
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photo', methods=["POST"])
def upload_file():
    for file in request.files.getlist('image'):
        print('..........................................')
        filename = file.filename
        destination =os.path.join('static', 'img', filename)
        file.save(destination)
        # just one image
        print(filename)
        X = []
        # Transformation in pixels
        X.append(np.array(Image.open(destination).resize((224,224))))
        X = np.array(X)
        #print(X.shape)
        X = X.astype('float32')
        X /= 255.
        #Load Model
        model = load_model(os.path.join('static', 'MODEL_olmos_classifier_5layers_15.h5'))
        #print("Loaded model")
        predictions = model.predict(X)
        #print(predictions)
        #if predictions[0][0] < 0.5:
        # color = "#246D5F"
        # else:
        #     color = "#FF4444"
        return render_template('index2.html', photo = filename, pred = round(predictions[0][0] * 100, 1))#, col = color)



if __name__ == '__main__':
    app.run()
