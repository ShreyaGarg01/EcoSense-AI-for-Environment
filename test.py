import pickle
import pandas as pd
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# Trained Models loaded


crop_recommendation_model_path = 'ModelsStore\Jaipur_maxtempC.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
future = pd.DataFrame({'ds': ['2023-05-05 7:00:00']})

my_prediction = crop_recommendation_model.predict(future)
print(my_prediction['yhat'])
x = '2023-05-05 '
x += current_time
# data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
future = pd.DataFrame({'ds': [x]})

my_prediction = crop_recommendation_model.predict(future)
print(my_prediction['yhat'])