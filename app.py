from flask import Flask, render_template, request, Markup, redirect, url_for
import numpy as np
import requests
import pickle
import io
from io import BytesIO
import base64
import pandas as pd
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
from send_predictions import predict_values

#  FLASK APP 
app = Flask(__name__)

# render home page
# @ app.route('/')
# def home():
#     title = 'Home'
#     return render_template('index.html', title=title)

@ app.route('/')
def start():
    title = 'Home'
    return render_template('index.html', title=title)


@ app.route('/home')
def home():
    title = 'Home'
    return render_template('index.html', title=title)


@ app.route('/pricing')
def price():
    title = 'Home'
    return render_template('pricing.html', title=title)



@ app.route('/about')
def about():
    title = 'about'
    return render_template('about.html', title=title)


@ app.route('/contact')
def contact():
    title = 'contact'
    return render_template('contact.html', title=title)


@ app.route('/services')
def services():
    title = 'services'
    return render_template('services.html', title=title)



@ app.route('/faq')
def faq():
    title = 'faq'
    return render_template('faq.html', title=title)


@ app.route('/blog-post')
def blog_post():
    title = 'blog-post'
    return render_template('blog-post.html', title=title)


@ app.route('/portfolio-item')
def portfolio_item():
    title = 'portfolio-item'
    return render_template('portfolio-item.html', title=title)


@ app.route('/blog-home-1')
def blog_home1():
    title = 'blog-home-1'
    return render_template('blog-home-1.html', title=title)


@ app.route('/blog-home-2')
def blog_home2():
    title = 'blog-home-2'
    return render_template('blog-home-2.html', title=title)



@ app.route('/portfolio-1-col')
def portfolio1col():
    title = 'portfolio-1-col'
    return render_template('portfolio-1-col.html', title=title)

# RENDER PREDICTION PAGES

@ app.route('/aqi')
def AQI():
    title = 'AQI'
    # if request.method == 'POST':
    #     location = str(request.form['Location'])
    #     date = request.form['Date']
    #     path = "AQI_Predictions/"
    #     path += str(location)
    #     path += "_AQI.csv"
    #     df = pd.read_csv(path, parse_dates=True, index_col = "ds")
    #     finalAQI = round(df._get_value(date, 'yhat'),2)
    #     predictions = predict_values(location, date)
    #     # cols = ['maxtempC', 'mintempC', 'humidity', 'precipMM', 'pressure', 'tempC', 'visibility', 'windspeedKmph']
    #     maxtemp = round(predictions[0],2)
    #     mintemp = round(predictions[1],2)
    #     humidity = round(predictions[2],2)
    #     preci = round(predictions[3],2)
    #     pressure = round(predictions[4],2)
    #     temp = round(predictions[5],2)
    #     visibility = round(predictions[6],2)
    #     windspeed = round(predictions[7],2)

    #     redirect(url_for('AQI', AQI=finalAQI, maxtemp = maxtemp, mintemp=mintemp,
    #                            humidity=humidity,preci=preci,pressure=pressure, temp=temp, visibility=visibility,
    #                            windspeed=windspeed,  title=title))
    #     redirect(url_for('AQI', AQI=finalAQI, maxtemp = maxtemp, mintemp=mintemp,
    #                            humidity=humidity,preci=preci,pressure=pressure, temp=temp, visibility=visibility,
    #                            windspeed=windspeed,  title=title))
    #     # return render_template('AQI.html', AQI=finalAQI, maxtemp = maxtemp, mintemp=mintemp,
    #     #                        humidity=humidity,preci=preci,pressure=pressure, temp=temp, visibility=visibility,
    #     #                        windspeed=windspeed,  title=title)
    return render_template('AQI.html',  title=title)


@ app.route('/result' ,  methods=['GET', 'POST'])
def result():
    title = 'AQI'
    if request.method == 'POST':
        location = str(request.form['Location'])
        date = request.form['Date']
        path = "AQI_Predictions/"
        path += str(location)
        path += "_AQI.csv"
        df = pd.read_csv(path, parse_dates=True, index_col = "ds")
        finalAQI = round(df._get_value(date, 'yhat'),2)
        predictions = predict_values(location, date)
        # cols = ['maxtempC', 'mintempC', 'humidity', 'precipMM', 'pressure', 'tempC', 'visibility', 'windspeedKmph']
        maxtemp = round(predictions[0],2)
        mintemp = round(predictions[1],2)
        humidity = round(predictions[2],2)
        preci = round(predictions[3],2)
        pressure = round(predictions[4],2)
        temp = round(predictions[5],2)
        visibility = round(predictions[6],2)
        windspeed = round(predictions[7],2)

        return redirect(url_for('AQI', result=finalAQI, maxtemp = maxtemp, mintemp=mintemp,
                               humidity=humidity,preci=preci,pressure=pressure, temp=temp, visibility=visibility,
                               windspeed=windspeed,  title=title))
        print(finalAQI)
        return redirect(url_for('.AQI', result=finalAQI))
        # return render_template('AQI.html', AQI=finalAQI, maxtemp = maxtemp, mintemp=mintemp,
        #                        humidity=humidity,preci=preci,pressure=pressure, temp=temp, visibility=visibility,
        #                        windspeed=windspeed,  title=title)
    return render_template('AQI.html',  title=title)


if __name__ == '__main__':
    app.run(debug = True)