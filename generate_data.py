import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==== PARÁMETROS ====
OUTPUT_FILE = "data/poly2Perfecto10p.csv"   # archivo de salida
DEPLOY_FILE = "data/data.csv"        # archivo de despliegue
DEPLOYMENT = True          # True si es para despliegue
N_SAMPLES = 100               # número de puntos
MODEL_TYPE = "poly"            # "linear" o "poly"
POLY_DEGREE = 5             # grado si es polinómico
NOISE_LEVEL = 5              # 0 = sin ruido, >0 = más error
SEED = 42                      # reproducibilidad
# ======================

def generate_data():
    np.random.seed(SEED)
    x = np.linspace(0, 10, N_SAMPLES)

    if MODEL_TYPE == "linear":
        y_true = 2 * x + 3
    elif MODEL_TYPE == "poly":
        # ejemplo: y = 0.1x³ - 0.5x² + 2x + 3
        coefs = [0.1, -0.5, 2, 3][:POLY_DEGREE + 1]
        y_true = sum(c * x**i for i, c in enumerate(reversed(coefs)))
    else:
        raise ValueError("MODEL_TYPE debe ser 'linear' o 'poly'")

    # Añadir ruido (controla el MSE)
    noise = np.random.normal(0, NOISE_LEVEL, size=N_SAMPLES)
    y = y_true + noise

    df = pd.DataFrame({"x": x, "y": y})
    df.to_csv(OUTPUT_FILE, index=False)

    # Si deploy es True, sobreescribir el archivo de despliegue
    if DEPLOYMENT:
        df.to_csv(DEPLOY_FILE, index=False)

    print(f"✅ Datos generados en {OUTPUT_FILE}")
    print(f"📈 Tipo: {MODEL_TYPE} | Ruido: {NOISE_LEVEL} | Muestras: {N_SAMPLES}")
    if DEPLOYMENT:
        print(f"📊 Archivo de despliegue: {DEPLOY_FILE}")
    else:
        print("📊 No se ha generado archivo de despliegue")

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.scatter(df['x'], df['y'], color='blue', label='Datos')

    # Añadir título y etiquetas
    plt.title('Gráfica de relación X vs Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)

    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    generate_data()
