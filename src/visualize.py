import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
data = pd.read_csv('c:/Users/mllavador/OneDrive - UPV/F_SIMARRO 25_26/MLOpsHelloWorld/HelloWorldMLOps/data/raw.csv')

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], color='blue', label='Datos')
plt.plot(data['x'], data['y'], color='red', label='Línea de tendencia')

# Añadir título y etiquetas
plt.title('Gráfica de relación X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()