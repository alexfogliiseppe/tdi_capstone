from flask import Flask, render_template

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #return 'A me funziona e a te no!'

if __name__ == '__main__':
    app.run()
