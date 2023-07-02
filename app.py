from flask import Flask, render_template, request, Markup
import numpy as np
import requests
import pickle
import io

import cv2
from io import BytesIO
import base64

# Trained Models loaded
# crop_recommendation_model_path = 'models/RandomForest.pkl'
# crop_recommendation_model = pickle.load(
#     open(crop_recommendation_model_path, 'rb'))

#  FLASK APP 
app = Flask(__name__)

# render home page
@ app.route('/')
def home():
    title = 'Home'
    return render_template('index.html', title=title)

@ app.route('/home')
def start():
    title = 'Home'
    return render_template('index.html', title=title)

# render crop recommendation form page
@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Crop Recommendation'
    return render_template('crop_recommendation.html', title=title)



# RENDER PREDICTION PAGES

@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])

        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        return render_template('crop_prediction.html', prediction=final_prediction, title=title)
        

if __name__ == '__main__':
    app.run(debug = True)