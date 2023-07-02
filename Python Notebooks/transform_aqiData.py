# Importing necessary libraries to conduct our analysis
# import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")
from IPython.display import HTML,display

warnings.filterwarnings("ignore")

df= pd.read_csv('..\Datasets\AQI_Data.csv',parse_dates=True)
df['Date'] = pd.to_datetime(df['Date'])

cities=pd.unique(df['City'])
column1= cities+'_AQI'
column2=cities+'_AQI_Bucket'
columns=[*column1,*column2]

final_df=pd.DataFrame(index=np.arange('2015-01-01','2020-08-01',dtype='datetime64[D]'),columns=column1)
for city,i in zip(cities,final_df.columns):
    n=len(np.array(df[df['City']==city]['AQI']))
    final_df[i][-n:]=np.array(df[df['City']==city]['AQI'])

final_df=final_df.astype('float64')
final_df['India_AQI']=final_df.mean(axis=1)
final_df.reset_index()

final_df.to_csv("AQI_CitywiseData.csv")