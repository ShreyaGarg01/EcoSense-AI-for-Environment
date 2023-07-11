from matplotlib import dates
from statsmodels.tsa.seasonal import seasonal_decompose
import datetime
# India_AQI=final_df['India_AQI']
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime, timedelta
def plot_vals_aqi_weekly(city,date):
    model_path = 'AQI_Predictions\\'
    model_path += city
    model_path += '_AQI.csv'
    # Convert the date string to a datetime object
    date = datetime.strptime(date, '%Y-%m-%d')
    start_of_week = date - timedelta(days=date.weekday())
    week_dates = [start_of_week + timedelta(days=i) for i in range(7)]
    df = pd.read_csv(model_path, parse_dates=True, index_col='ds')
    df = df[start_of_week:week_dates[6]]
   
    y = df['yhat']
   
    sns.set(style="darkgrid")  # Set the style of the plot
    plt.figure(figsize=(8, 6))  # Set the figure size
    fig = sns.lineplot(y, color='blue', linewidth=2.5, marker='o')
    
    plt.xlabel('Date')
    plt.ylabel('AQI (ppm)')
    plt.title('Line Plot of AQI for the week')

    return fig


def plot_vals_AQI_yearly(city,date):
    model_path = 'AQI_Predictions\\'
    model_path += city
    model_path += '_AQI.csv'
    # Convert the date string to a datetime object
    date = datetime.strptime(date, '%Y-%m-%d')
    start_of_week = date - timedelta(days=date.weekday())
    week_dates = [start_of_week + timedelta(days=i) for i in range(7)]
    df = pd.read_csv(model_path, parse_dates=True, index_col='ds')
   
    df = df.groupby(pd.Grouper(freq='y')).mean()
    df = df[:'2023']

    # x = df['ds']
    y = df['yhat']
    
    sns.set(style="darkgrid")  # Set the style of the plot
    plt.figure(figsize=(8, 6))  # Set the figure size
    # fig = sns.barplot(y, color='blue')
    fig =sns.barplot(x = df.index.year, y = y,palette="GnBu_d", )

    
    plt.xlabel('Date')
    plt.ylabel('AQI (ppm)')
    plt.title('Historical Trend of Mean AQI')

    return fig

