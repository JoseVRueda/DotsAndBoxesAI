# Función para verificar si todas las posiciones están ocupadas
def todas_posiciones_ocupadas(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == '0':
                return False
    return True

# Función para dibujar el tablero
def dibujar_tablero(tablero, completados,puntajes):
    print("\nTurno de:",jugador_actual)
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if (i % 2 == 1 and j % 2 == 1 and tablero[i][j] == ' ') or (i, j) in completados:
                print(' ', completados[(i, j)], end='  ')
            else:
                print(tablero[i][j], end='')
        print()
    print()
    for jugador, puntaje in puntajes.items():
        print(f"Puntaje de jugador {jugador}: {puntaje}")

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
    if fila % 2 == 0: # Si la fila es par
        if fila == 0:
            if tablero[fila + 1][columna - 1] != "0" and tablero[fila + 1][columna + 1] != "0" and tablero[fila + 2][columna] != "0":
                completados[(fila + 1, columna)] = jugador
                puntajes[jugador] += 1
                print('comp0')
                completado = True
        elif fila == 6:
            if tablero[fila - 1][columna - 1] != "0" and tablero[fila - 1][columna + 1] != "0" and tablero[fila - 2][columna] != "0":
                completados[(fila - 1, columna)] = jugador
                puntajes[jugador] += 1
                print('comp6')
                completado = True
        else: #No son filas exteriores
            if tablero[fila - 1][columna - 1] != "0" and tablero[fila - 1][columna + 1] != "0" and tablero[fila - 2][columna] != "0":
                completados[(fila - 1, columna)] = jugador
                puntajes[jugador] += 1
                print('comp arriba')
                completado = True
            elif tablero[fila + 1][columna - 1] != "0" and tablero[fila + 1][columna + 1] != "0" and tablero[fila + 2][columna] != "0":
                completados[(fila + 1, columna)] = jugador
                puntajes[jugador] += 1
                print('comp abajo')
                completado = True
    else:  # Si la fila es impar
        if columna == 0:
            if tablero[fila - 1][columna + 1] != "0" and tablero[fila + 1][columna + 1] != "0" and tablero[fila][columna + 2] != "0":
                completados[(fila, columna + 1)] = jugador
                puntajes[jugador] += 1
                print('comp0lateral')
                completado = True
        elif columna == 6:
            if tablero[fila - 1][columna - 1] != "0" and tablero[fila + 1][columna - 1] != "0" and tablero[fila][columna - 2] != "0":
                completados[(fila, columna - 1)] = jugador
                puntajes[jugador] += 1
                print('comp6lateral')
                completado = True
        else: #No son columnas exteriores
            if tablero[fila - 1][columna - 1] != "0" and tablero[fila + 1][columna - 1] != "0" and tablero[fila][columna - 2] != "0":
                completados[(fila, columna - 1)] = jugador
                puntajes[jugador] += 1
                print('compizq')
                completado = True
            elif tablero[fila - 1][columna + 1] != "0" and tablero[fila + 1][columna + 1] != "0" and tablero[fila][columna + 2] != "0":
                completados[(fila, columna + 1)] = jugador
                puntajes[jugador] += 1
                print('compder')
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

# Definir jugadores
jugadores = ['A', 'B']
puntajes = {jugadores[0]: 0, jugadores[1]: 0}
jugador_actual = jugadores[0]  # Comienza el jugador A

# Dibujar el tablero inicial
dibujar_tablero(tablero, {}, puntajes)

# Inicializar cuadrados completados
completados = {}
puntaje_anterior = 0

# Continuar hasta que todas las posiciones estén ocupadas
while not todas_posiciones_ocupadas(tablero):
    # Solicitar al usuario que ingrese la fila y la columna
    fila = int(input("\nIngrese la fila (0-6): "))
    columna = int(input("Ingrese la columna (0-6): "))

    # Verificar si la posición seleccionada es válida y dibujar la línea
    if fila >= 0 and fila < 7 and columna >= 0 and columna < 7 and tablero[fila][columna] == "0":
        dibujar_linea(tablero, fila, columna, jugador_actual, completados)
        # Verificar si el jugador actual completó un cuadrado para darle un turno adicional
        if puntajes[jugador_actual] > puntaje_anterior:
            print("¡El jugador", jugador_actual, "ha completado un cuadrado y tiene un turno adicional!")
        else:
            jugador_actual = jugadores[(jugadores.index(jugador_actual) + 1) % len(jugadores)]
        # Actualizar puntaje_anterior después de cada turno
        puntaje_anterior = puntajes[jugador_actual]
        dibujar_tablero(tablero, completados, puntajes)
    else:
        print("Posición inválida o ya ocupada.")
    
ganador = max(puntajes, key=puntajes.get)
print("¡Todas las posiciones han sido ocupadas!")
print("El ganador es:", ganador)

