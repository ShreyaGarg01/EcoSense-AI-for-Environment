# %%
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tools.eval_measures import rmse
from prophet import Prophet

# %%
def get_df_for_prediction(path, x):
    df = pd.read_csv(path, parse_dates=['date_time'], index_col='date_time')
    df = df.loc[:,[x]]
    print(x)
    return df

# %%
# India_AQI=final_df['India_AQI']
def plot_seasonal_decompose(df):
    result=seasonal_decompose(df,model='multiplicative')
    result.plot()
    ax=result.seasonal.plot(xlim=['2015-01-01','2015-01-02'],figsize=(20,8),lw=2)
    ax.yaxis.grid(True)
    ax.xaxis.grid(True)


# %%

def test_train_splitting(df):
    df=df.reset_index()
    df.columns=['ds','y']
    train = df[df['ds'] < pd.Timestamp('2019-01-01')]
    test = df[df['ds'] >= pd.Timestamp('2019-01-01')]
    return train, test


# %%
# future = m.make_future_dataframe(periods=12,freq = 'MS')
def predict(train,i, test):
    m = Prophet(seasonality_mode='multiplicative', yearly_seasonality= True, weekly_seasonality=False, daily_seasonality= True)
    m.add_seasonality(name='hourly', period=1/24, fourier_order=5)
    m.fit(train)
    future = m.make_future_dataframe(periods=365*4*24, freq='H') 
    forecast = m.predict(future)
    forecast.to_csv("fore.csv")
    fig1 = m.plot(forecast)
    plt.legend(['Actual', 'Prediction', 'Uncertainty interval'])
    # # plt.savefig('components'+i+'.png')
    plt.show()
    fig2 = m.plot_components(forecast)
    plt.show()
    # predictions = forecast.iloc[-len(test):]['yhat']
    # actuals = test['y']
    # mse = rmse(predictions, actuals)
    # print(f"RMSE: {round(mse)}")    
    return forecast, 0

#%%
df = pd.read_csv(".\Datasets\jaipur.csv", parse_dates=['date_time'], index_col='date_time')
x = df.columns[:1]
params = []
rmses = []
figs = []
graphs = []

for i in x:
    df = get_df_for_prediction(".\Datasets\jaipur.csv", i)
    train, test = test_train_splitting(df)
    forecast, rms = predict(train, i, test)
    print(forecast)

    

df = pd.DataFrame(list(zip(params, rmses)),
                columns =['Parameter', 'RMSE'])

df.to_csv('Predictions.csv')
