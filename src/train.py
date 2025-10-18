import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

def train(data_path, model_path):

    df = pd.read_csv(data_path)
    X, y = df[["x"]], df["y"]
    
    # model = LinearRegression()
    
    # Pipeline: transforma x -> x^n y entrena regresión lineal sobre esas features
    model = Pipeline([
        ("poly", PolynomialFeatures(degree=2)),
        ("linreg", LinearRegression())
    ])

    model.fit(X, y)
    pickle.dump(model, open(model_path, "wb"))
    print(f"Modelo entrenado y guardado en {model_path}")

