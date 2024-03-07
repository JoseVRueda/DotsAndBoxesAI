# Función para verificar si todas las posiciones están ocupadas
def todas_posiciones_ocupadas(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == '0':
                return False
    return True

# Función para dibujar el tablero
def dibujar_tablero(tablero, completados):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if (i % 2 == 1 and j % 2 == 1 and tablero[i][j] == ' ') or (i, j) in completados:
                print(completados[(i, j)], end='')
            else:
                print(tablero[i][j], end='')
        print()

# Función para dibujar una línea en la posición dada
def dibujar_linea(tablero, fila, columna, jugador, completados):
    if fila % 2 == 0:
        tablero[fila][columna] = "-"
    else:
        tablero[fila][columna] = "|"
    completar_cuadrados(tablero, fila, columna, jugador, completados)

# Función para completar los cuadrados
def completar_cuadrados(tablero, fila, columna, jugador, completados):
    completado = False
    if fila % 2 == 0:  # Si la fila es par, comprobar cuadrado arriba y abajo
        if fila > 0 and tablero[fila - 1][columna] != "0" and tablero[fila - 1][columna + 1] != "0" and \
                tablero[fila + 1][columna] != "0" and tablero[fila + 1][columna + 1] != "0":
            completados[(fila - 1, columna)] = jugador
            completado = True
    else:  # Si la fila es impar, comprobar cuadrado a la izquierda y derecha
        if columna > 0 and tablero[fila][columna - 1] != "0" and tablero[fila - 1][columna] != "0" and \
                tablero[fila][columna + 1] != "0" and tablero[fila + 1][columna] != "0":
            completados[(fila, columna - 1)] = jugador
            completado = True
    if completado:
        print(f"\n¡Cuadrado completado por el jugador {jugador}!")

# Crear un tablero representado como una lista de listas
tablero = []
for i in range(7):
    if i % 2 == 0:
        tablero.append(['+  ', '0', '  +  ', '0', '  +  ', '0', '  +'])
    else:
        tablero.append(['0', '     ', '0', '     ', '0', '     ', '0'])

# Dibujar el tablero inicial
dibujar_tablero(tablero, {})

# Definir jugadores
jugadores = ['  A  ', '  B  ']
jugador_actual = jugadores[0]  # Comienza el jugador A

# Inicializar cuadrados completados
completados = {}

# Continuar hasta que todas las posiciones estén ocupadas
while not todas_posiciones_ocupadas(tablero):
    # Solicitar al usuario que ingrese la fila y la columna
    fila = int(input("\nIngrese la fila (0-6): "))
    columna = int(input("Ingrese la columna (0-6): "))

    # Verificar si la posición seleccionada es válida y dibujar la línea
    if fila >= 0 and fila < 7 and columna >= 0 and columna < 7 and tablero[fila][columna] == "0":
        dibujar_linea(tablero, fila, columna, jugador_actual, completados)
        print("Tablero actualizado:")
        dibujar_tablero(tablero, completados)
        # Cambiar al siguiente jugador
        jugador_actual = jugadores[(jugadores.index(jugador_actual) + 1) % len(jugadores)]
    else:
        print("Posición inválida o ya ocupada.")

print("¡Todas las posiciones han sido ocupadas!")
