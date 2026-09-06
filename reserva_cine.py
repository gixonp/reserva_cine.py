# Programa: Reserva de un asiento en sala de cine
# Autor: Gixon Pinargote
# Este programa permite reservar un asiento en una sala de cine
# de 3 filas por 4 columnas y mostrar el estado de todos los asientos.

# Crear la matriz de 3 filas y 4 columnas.
# 0 representa un asiento libre.
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila y la columna del asiento.
fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))

# Verificar que los índices estén dentro del rango permitido.
if 0 <= fila <= 2 and 0 <= columna <= 3:

    # Verificar si el asiento está libre.
    if asientos[fila][columna] == 0:

        # Marcar el asiento como reservado.
        asientos[fila][columna] = 1

        print("\n¡Asiento reservado correctamente!")

    else:
        print("\nEl asiento ya está reservado.")

else:
    print("\nFila o columna fuera del rango permitido.")

# Mostrar el estado completo de la sala.
print("\nEstado de la sala:")
print("-------------------")

# Recorrer las filas de la matriz.
for i in range(3):

    # Recorrer las columnas de cada fila.
    for j in range(4):
        print(asientos[i][j], end=" ")

    # Salto de línea al terminar cada fila.
    print()

print("-------------------")
print("0 = Libre | 1 = Reservado")