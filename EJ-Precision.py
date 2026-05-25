# Programa: Precisión de Máquina
# Descripción:
# Este programa calcula la precisión de máquina (epsilon)
# Se hara usando diviisiones sucesivas entre 2

import sys

# Valor inicial
epsilon = 1.0

# Proceso iterativo
while (1.0 + epsilon) != 1.0:
    epsilon = epsilon / 2

# Recuperar el último valor válido
epsilon = epsilon * 2

# Mostrar resultados
print("Resultado")
print("-" * 40)
print("Precisión:", epsilon)
print("Precisión del sistema:", sys.float_info.epsilon)
