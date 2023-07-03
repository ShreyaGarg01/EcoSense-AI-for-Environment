from flask import Flask, render_template, request, Markup
import numpy as np
import requests
import pickle
import io
from io import BytesIO
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
from IPython.display import HTML,display
from prophet import Prophet
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
warnings.filterwarnings("ignore")

#  FLASK APP 
app = Flask(__name__)

# render home page
# @ app.route('/')
# def home():
#     title = 'Home'
#     return render_template('index.html', title=title)

@ app.route('/home')
def start():
    title = 'Home'
    return render_template('index.html', title=title)


# RENDER PREDICTION PAGES

@ app.route('/' ,  methods=['GET', 'POST'])
def AQI():
    title = 'AQI'
    if request.method == 'POST':
        location = str(request.form['Location'])
        date = request.form['Date']
        path = "AQI_Predictions/"
        path += str(location)
        path += "_AQI.csv"
        df = pd.read_csv(path, parse_dates=True, index_col = "ds")
        final = df._get_value(date, 'yhat')
        return render_template('AQI.html', prediction=final, title=title)
    return render_template('AQI.html', prediction=1, title=title)


@ app.route('/weather' ,  methods=['GET', 'POST'])
def weather():
    title = 'AQI'
    if request.method == 'POST':
        location = str(request.form['Location'])
        date = request.form['Date']
        path = "AQI_Predictions/"
        path += str(location)
        path += "_AQI.csv"
        df = pd.read_csv(path, parse_dates=True, index_col = "ds")
        final = df._get_value(date, 'yhat')
        return render_template('AQI.html', prediction=final, title=title)
    return render_template('AQI.html', prediction=1, title=title)
        

if __name__ == '__main__':
    app.run(debug = True)