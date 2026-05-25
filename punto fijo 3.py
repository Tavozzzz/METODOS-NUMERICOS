import math
import pandas as pd
import matplotlib.pyplot as plt

# Función g(x)
def g(x):
    return math.cos(x)

# Derivada de g(x)
def g_derivada(x):
    return -math.sin(x)

# Valor inicial
x0 = 0.5

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

# Evaluación del criterio de convergencia
valor_derivada = abs(g_derivada(x1))

print("\n|g'(x)| =", valor_derivada)

if valor_derivada < 1:
    print("El criterio de convergencia se cumple.")
else:
    print("El criterio de convergencia NO se cumple.")

# Gráfica de convergencia
plt.plot(range(1, len(errores)+1), errores, marker='o')

plt.yscale('log')

plt.xlabel('Iteración')
plt.ylabel('Error')
plt.title('Convergencia del Método de Punto Fijo')

plt.grid(True)

plt.show()
