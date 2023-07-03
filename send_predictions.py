import pickle
import pandas as pd
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

locations = ['Jaipur', 'Bengaluru', 'Bombay', 'Delhi','Hyderabad','Kanpur','Nagpur','Pune']
# Trained Models loaded

def predict_values(city, date):
    
    cols = ['maxtempC', 'mintempC', 'humidity', 'precipMM', 'pressure', 'tempC', 'visibility', 'windspeedKmph']
    predictions = []

    for col in cols:
        model_path = 'ModelsStore\\'
        model_path += city
        model_path += '_'
        model_path += col
        model_path += '.pkl'
        model = pickle.load(open(model_path, 'rb'))

        x = date
        x += " "
        x += current_time
        # data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        future = pd.DataFrame({'ds': [x]})

        my_prediction = model.predict(future)
        print(my_prediction['yhat'][0])
        predictions.append(my_prediction['yhat'][0])
    
    return predictions