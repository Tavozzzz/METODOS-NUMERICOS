# Programa Aproximación de PI con la serie de Leibniz
# Descripción:
# Aproxima el valor de pi utilizando la serie de Leibniz

import math
import pandas as pd
import matplotlib.pyplot as plt

# Valores de N
valores_n = [10, 100, 1000, 10000]

# Valor real de pi
pi_real = math.pi

# Listas para almacenar resultados
pi_aproximado = []
error_absoluto = []
error_relativo = []
error_cuadratico = []

# Cálculos
for N in valores_n:

    suma = 0

    for n in range(N):
        suma += ((-1) ** n) / (2 * n + 1)

    pi_calc = 4 * suma

    # Errores
    err_abs = abs(pi_real - pi_calc)
    err_rel = err_abs / abs(pi_real)
    err_cua = (pi_real - pi_calc) ** 2

    # Guardar resultados
    pi_aproximado.append(pi_calc)
    error_absoluto.append(err_abs)
    error_relativo.append(err_rel)
    error_cuadratico.append(err_cua)

# Crear tabla
tabla = pd.DataFrame({
    "N": valores_n,
    "Pi Aproximado": pi_aproximado,
    "Error Absoluto": error_absoluto,
    "Error Relativo": error_relativo,
    "Error Cuadrático": error_cuadratico
})

# Mostrar tabla
print("\nReesultados")
print("-" * 80)
print(tabla)

# Graficar errores
plt.plot(valores_n, error_absoluto, marker='o', label='Error Absoluto')
plt.plot(valores_n, error_relativo, marker='o', label='Error Relativo')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Número de términos (N)')
plt.ylabel('Error')
plt.title('Errores en la aproximación de PI')
plt.legend()
plt.grid(True)

plt.show()
