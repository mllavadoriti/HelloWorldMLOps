import pickle
import pandas as pd

def predict(model_path, x):
    model = pickle.load(open(model_path, "rb"))
    return model.predict([[x]])[0]
