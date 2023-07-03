# %%
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tools.eval_measures import rmse
from prophet import Prophet
import pickle

# %%
# future = m.make_future_dataframe(periods=12,freq = 'MS')
def predict(path, i, loct):
    df = pd.read_csv(path, parse_dates=['date_time'], index_col='date_time')
    df = df.loc[:,[i]]
    df=df.reset_index()
    df.columns=['ds','y']
    m = Prophet(seasonality_mode='multiplicative')
    m.fit(df)
    a = ".\\ModelsStore\\"
    a += loct
    a += "_"
    a += i
    a += ".pkl"    
    model = open(a, 'wb')
    pickle.dump(m, model)
    model.close()

#%%

locations = ['Jaipur', 'Bengaluru', 'Bombay', 'Delhi','Hyderabad','Kanpur','Nagpur','Pune']
# locations = ['\Jaipur']

df = pd.read_csv(".\\Datasets\\Jaipur.csv", parse_dates=['date_time'], index_col='date_time')
x = df.columns
for loc in locations:
    path = ".\\Datasets\\" 
    path += loc
    path += ".csv"
    for i in x:
        predict(path, i, loc)
