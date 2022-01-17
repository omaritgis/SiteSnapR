from flask import Flask, render_template, request
from snap import UIFlow
import requests
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/snap', methods=['POST'])
def snap():
    protocol = request.form['protocol']
    url = request.form['url']
    url = protocol + url
    ui = UIFlow()
    ui.browserOpens(url)
    ui.pictureSnapped()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'screenshots.png')
    return render_template('index.html', user_image=full_filename)

if __name__ == '__main__':
    print("test")
    app.run()