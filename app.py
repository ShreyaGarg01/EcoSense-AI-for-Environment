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
from plot_graph import plot_vals_aqi_weekly
from plot_graph import plot_vals_AQI_yearly
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import json
from generate_json import make_json

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
    active_page = 'home'
    return render_template('index.html', title=title, active_page=active_page)


@ app.route('/home')
def home():
    title = 'Home'
    active_page = 'home'
    return render_template('index.html', title=title, active_page=active_page)



@ app.route('/quotes')
def quotes():
    title = 'quotes'
    quotes = ['EcoSense is an AI system that will provide real-time insights and visualizations into the current state of the environment. This information will help people understand the impact of human activity on the environment and take action to protect it.', 
              'The proposed project, EcoSense, will address the societal challenge of climate change and environmental degradation.',
              ' Climate change is one of the most pressing issues of our time, and it is having a devastating impact on our planet. EcoSense will help us to understand the impact of climate change and other environmental problems, and it will empower us to take action to protect our planet.',
              'With EcoSense, people will be able to see the impact of their actions on the environment and make informed decisions about how to live more sustainably. It is a system that will help us understand our planet and take action to protect it.',
              'EcoSense is a tool that can help us to create a more sustainable future. It is the future of environmental monitoring.',
              'It is still a protype and hence has a limited data.']
    active_page = 'quotes'
    return render_template('quotes.html',quotes=quotes, title=title, active_page=active_page)


@ app.route('/india_analysis')
def blog_home2():
    title = 'india_analysis'
    active_page = 'india'
    return render_template('india_analysis.html', title=title, active_page=active_page)


@ app.route('/result2',  methods=['GET', 'POST'])
def analyse():
    title = 'india_analysis'
    active_page = 'india'
    title = 'AQI'
    if request.method == 'POST':
        choice = str(request.form['Location'])
        
        # cols = ['maxtempC', 'mintempC', 'humidity', 'precipMM', 'pressure', 'tempC', 'visibility', 'windspeedKmph']
        if (choice=="tree"):
            return redirect(url_for('india-analysis', file='/static/images/trees.png'), c = "tree")      
        
        
    return render_template('india_analysis.html', title=title, active_page=active_page)


# RENDER PREDICTION PAGES


@ app.route('/result' ,  methods=['GET', 'POST'])
def result():
    title = 'Predictions'
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
        fig = plot_vals_aqi_weekly(location,date)
        
        # fig.show()
        plot_filename_aqi = 'static/line_plot.png'
        plt.savefig(plot_filename_aqi)
        plot_filename_aqi = '/static/line_plot.png'
        plt.close()
        
        fig2 = plot_vals_AQI_yearly(location,date)
        plot_filename_aqi_yearly = 'static/bar_plot.png'
        plt.savefig(plot_filename_aqi_yearly)
        plot_filename_aqi_yearly = '/static/bar_plot.png'
        make_json(path)
        with open('city_AQI.json') as f:
            data = json.load(f)
       
        return render_template('index.html', aqi=finalAQI, result=finalAQI, maxtemp = maxtemp, mintemp=mintemp,
                            humidity=humidity,preci=preci,pressure=pressure, temp=temp, visibility=visibility,
                            windspeed=windspeed,  title=title, plot_filename=plot_filename_aqi, 
                            bar_plot=plot_filename_aqi_yearly, city=location, data = data )
        
    return render_template('index.html',  title=title)


if __name__ == '__main__':
    app.run(debug = True)