import os
from funciones import suma, resta, multiplicacion

# Crear la carpeta resultados si no existe
if not os.path.exists('resultados'):
    os.makedirs('resultados')

# Generar un archivo de texto dentro de la carpeta
with open('resultados/log_operaciones.txt', 'w') as f:
    f.write(f"Suma: {suma(10, 5)}\n")
    f.write(f"Resta: {resta(10, 5)}\n")
    f.write(f"Multiplicación: {multiplicacion(10, 5)}\n")



print("Programa ejecutado: Archivo generado en la carpeta resultados/")

import 