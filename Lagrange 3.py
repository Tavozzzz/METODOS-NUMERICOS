import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Función original
def f(x):
    return np.exp(-x) - x

# Puntos para interpolación
x_puntos = np.array([0, 0.33, 0.66, 1])
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

# Valores para gráficas
x_vals = np.linspace(0, 1, 400)

f_vals = f(x_vals)

p_vals = [lagrange(x, x_puntos, y_puntos) for x in x_vals]

# Aproximación de raíz
indice = np.argmin(np.abs(p_vals))

raiz = x_vals[indice]

# Valor real aproximado
raiz_real = 0.567143

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

# Gráfica función y polinomio
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

# Gráfica de errores
errores = abs(f_vals - p_vals)

plt.plot(x_vals, errores)

plt.xlabel('x')
plt.ylabel('Error')

plt.title('Error de Interpolación')

plt.grid(True)

plt.show()
