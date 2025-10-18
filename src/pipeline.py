from src.train import train
from src.predict import predict
from src.evaluate import evaluate

def run_pipeline():
    data="data/data.csv"
    model = "model/model.pkl"
    metrics = "metrics/metrics.txt"

    train(data, model)
    evaluate(model, data, metrics)
    print(f"Predicción ejemplo para x=50: {predict(model, 50)}")