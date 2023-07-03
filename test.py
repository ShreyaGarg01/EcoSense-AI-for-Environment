import pickle
import pandas as pd

# Trained Models loaded
crop_recommendation_model_path = 'ModelsStore\Jaipur_maxtempC.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
future = pd.DataFrame({'ds': ['2023-05-05 7:00:00']})

my_prediction = crop_recommendation_model.predict(future)
print(my_prediction['yhat'])

# data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
future = pd.DataFrame({'ds': ['2023-05-05 9:00:00']})

my_prediction = crop_recommendation_model.predict(future)
print(my_prediction['yhat'])