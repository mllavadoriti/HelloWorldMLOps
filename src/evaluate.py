import pickle, pandas as pd
from sklearn.metrics import mean_squared_error

def evaluate(model_path, data_path, metrics_path):
    model = pickle.load(open(model_path, "rb"))
    df = pd.read_csv(data_path)
    y_pred = model.predict(df[["x"]])
    mse = mean_squared_error(df["y"], y_pred)
    with open(metrics_path, "w") as f:
        f.write(f"MSE: {mse}\n")
    print(f"Métricas guardadas en {metrics_path}")
    print(f"MSE: {mse}")