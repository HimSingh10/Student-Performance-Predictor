import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict_performance(hours, sleep, activities):
    activities = 1 if activities == "Yes" else 0
    data = np.array([[hours, sleep, activities]])
    return model.predict(data)[0]