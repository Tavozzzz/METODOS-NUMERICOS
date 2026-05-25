import math
import pandas as pd
import matplotlib.pyplot as plt

# Función g(x)
def g(x):
    return math.exp(x) / 4

# Valor inicial
x0 = 1.0

# Tolerancia
tol = 1e-5

# Variables
error = 1
iteracion = 1

# Listas para tabla y gráfica
datos = []
errores = []

# Método iterativo
while error > tol:

    x1 = g(x0)

    error = abs(x1 - x0)

    # Guardar datos
    datos.append([
        iteracion,
        x0,
        x1,
        error
    ])

    errores.append(error)

    # Actualizar valor
    x0 = x1

    iteracion += 1

# Crear tabla
tabla = pd.DataFrame(
    datos,
    columns=[
        "Iteración",
        "x_n",
        "x_(n+1)",
        "Error"
    ]
)

# Mostrar tabla
print("\nTABLA DE ITERACIONES")
print(tabla)

# Resultado final
print("\nRaíz aproximada:", x1)
print("Número de iteraciones:", iteracion - 1)

# Gráfica de convergencia
plt.plot(range(1, len(errores)+1), errores, marker='o')

plt.yscale('log')

plt.xlabel('Iteración')
plt.ylabel('Error')
plt.title('Convergencia del Método de Punto Fijo')

plt.grid(True)

plt.show()
