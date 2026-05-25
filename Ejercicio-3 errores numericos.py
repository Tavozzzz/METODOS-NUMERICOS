

# Primer caso
x1 = 1.0000001
y1 = 1.0000000

valor_exacto_1 = 0.0000001

diferencia1 = x1 - y1

error_absoluto1 = abs(valor_exacto_1 - diferencia1)
error_relativo1 = error_absoluto1 / abs(valor_exacto_1)

# Segundo caso
x2 = 1.000000000000001
y2 = 1.000000000000000

valor_exacto_2 = 0.000000000000001

diferencia2 = x2 - y2

error_absoluto2 = abs(valor_exacto_2 - diferencia2)
error_relativo2 = error_absoluto2 / abs(valor_exacto_2)

# Mostrar resultados
print("Resultado")
print("-" * 50)

print("\nPrimer caso")
print("Diferencia:", diferencia1)
print("Error absoluto:", error_absoluto1)
print("Error relativo:", error_relativo1)

print("\nSegundo caso")
print("Diferencia:", diferencia2)
print("Error absoluto:", error_absoluto2)
print("Error relativo:", error_relativo2
