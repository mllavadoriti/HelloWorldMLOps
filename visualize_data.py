import pandas as pd
import matplotlib.pyplot as plt

# ==== PARÁMETROS ====
DATA_FILE = 'data/data.csv'  # Ruta al archivo CSV
# ======================

# Leer el archivo CSV
data = pd.read_csv(DATA_FILE)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], color='blue', label='Datos')

# Añadir título y etiquetas
plt.title('Gráfica de relación X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()