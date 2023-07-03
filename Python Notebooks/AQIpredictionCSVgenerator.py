# %%
# Importing necessary libraries to conduct our analysis
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

# %%
#Formatting necessary to Prophet:

def create_csv(loc):
    # India_AQI2 = final_df[loc]['2018-01':]

    India_AQI2 = final_df[loc]['2018-01':'2020-05']
    India_AQI2=India_AQI2.reset_index()
    India_AQI2.columns=['ds','y']
    m = Prophet(seasonality_mode='multiplicative',yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
    
    m.fit(India_AQI2)
    future = m.make_future_dataframe(periods=365*4)
    forecast = m.predict(future)
    fig = m.plot(forecast)
    plt.legend(['Actual', 'Prediction', 'Uncertainty interval'])
    plt.show()
    pred = forecast[['ds','yhat']]
    pred.to_csv("./AQI_Predictions/" + loc + ".csv")




# %%
# m.plot_components(forecast);
final_df= pd.read_csv('.\Datasets\AQI_CitywiseData.csv',parse_dates=True, index_col = "Date")
final_df = final_df.interpolate(method="linear")
final_df.fillna(method="bfill", inplace=True)
# India_AQI=final_df['India_AQI']
# locs = final_df.columns
locs = ['Mumbai_AQI']
for loc in locs:
    create_csv(loc)


