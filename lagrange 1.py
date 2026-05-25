import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Función original
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

# Puntos seleccionados
x_puntos = np.array([1, 2, 3])
y_puntos = f(x_puntos)

# Polinomio de Lagrange
def lagrange(x, xp, yp):

    n = len(xp)
    P = 0

    for i in range(n):

        Li = 1

        for j in range(n):

            if i != j:
                Li *= (x - xp[j]) / (xp[i] - xp[j])

        P += yp[i] * Li

    return P

# Valores para gráfica
x_vals = np.linspace(1, 3, 400)

f_vals = f(x_vals)

p_vals = [lagrange(x, x_puntos, y_puntos) for x in x_vals]

# Aproximación de raíz
raiz = 1

# Valor real
raiz_real = 1

# Errores
error_abs = abs(raiz_real - raiz)
error_rel = error_abs / abs(raiz_real)
error_cua = (raiz_real - raiz)**2

# Tabla de resultados
tabla = pd.DataFrame({
    "Raíz Aproximada": [raiz],
    "Error Absoluto": [error_abs],
    "Error Relativo": [error_rel],
    "Error Cuadrático": [error_cua]
})

print("\nRESULTADOS")
print(tabla)

# Gráfica
plt.plot(x_vals, f_vals, label='f(x)')
plt.plot(x_vals, p_vals, '--', label='Polinomio de Lagrange')

plt.scatter(x_puntos, y_puntos)

plt.axhline(0)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Lagrange')

plt.legend()
plt.grid(True)

plt.show()
