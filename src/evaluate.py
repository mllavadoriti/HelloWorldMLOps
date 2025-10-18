import pickle, pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def evaluate(model_path, data_path, metrics_path):
    model = pickle.load(open(model_path, "rb"))
    df = pd.read_csv(data_path)
    y_pred = model.predict(df[["x"]])
    mse = mean_squared_error(df["y"], y_pred)
    with open(metrics_path, "a") as f:
        f.write(f"MSE: {mse}\n")
    print(f"Métricas guardadas en {metrics_path}")
    print(f"MSE: {mse}")

    # Gráfica 2D
    plt.figure(figsize=(6,4))
    plt.plot(df["x"], y_pred, color="red", label="Predicción", linewidth=2)
    plt.scatter(df["x"], df["y"], color="blue", label="Datos reales")
    plt.title(f"Evaluación del modelo (MSE={mse:.4f})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()