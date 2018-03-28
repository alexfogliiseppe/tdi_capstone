import os
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES


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
        # X = []
        # # Transformation in pixels
        # X.append(np.array(Image.open(destination).resize((150,150))))
        # X = np.array(X)
        # print(X.shape)
        # X = X.astype('float32')
        # X /= 255
        # #Load Model
        # model = load_model(os.path.join('static', 'model.h5'))
        # print("Loaded model")
        # predictions = model.predict(X)
        # print(predictions)
        # if predictions[0][0] < 0.5:
        #     color = "#246D5F"
        # else:
        #     color = "#FF4444"
        return render_template('index2.html', photo = filename)#, pred = round(predictions[0][0] * 100, 1), col = color)



if __name__ == '__main__':
    app.run()
