import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd

def train(data_path, model_path):
    df = pd.read_csv(data_path)
    X, y = df[["x"]], df["y"]
    model = LinearRegression()
    model.fit(X, y)
    pickle.dump(model, open(model_path, "wb"))
    print(f"Modelo entrenado y guardado en {model_path}")

