from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import secure_filename
from app.preprocess import cv_equalize
from scipy.misc import imread
#from base64 import b64encode
from app import app
import pandas as pd
import numpy as np
import pickle
import re
import os


ALLOWED_EXTENSIONS = set(['png', 'jpg'])
filename = secure_filename("tmp.jpg")
model_path = os.path.join("app/model", "weatherml.pkl")


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/index')
def index():
  return render_template('index.html')



#Takes the original weather data loaded as Dataframe and converts to ML friendly format
def dataFrame2Array(images, train_set):
  # reshape to (_,49152) (192x256 image to 1-d)

  for i in range(train_set.shape[0]):
      images[i] = train_set.image.iloc[i] / 255

@app.route('/prediction')
def prediction():

  image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  image_data = pd.DataFrame(columns=("image", "name"))
  X_test  = np.zeros((1,49152), dtype=np.float32)

  cv_equalize(image_path)

  image = imread(image_path)
  image_data.loc[0] = [imread(image_path).ravel(), filename]

  dataFrame2Array(X_test, image_data)
  
  with open(model_path, 'rb') as pk:
    pkl_model = pickle.load(pk)

  prediction = pkl_model.predict(X_test)

  #delete file from tmp directory when done
  #os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

  return render_template('results.html', prediction=prediction[0])



#Function from http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET','POST'])
def upload():

  if request.method == 'POST':
    if 'file' not in request.files:
      flash("No file received")
      return render_template('home.html')

  file = request.files['file']

  if file and allowed_file(file.filename):
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return "OK"

  else:
      flash("Only .png and .jpg file formats are allowed")
      return render_template('home.html')
