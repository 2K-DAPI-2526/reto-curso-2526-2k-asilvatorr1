#parte 1
def crear_tablero():
    return [
        ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
        ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
        ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    ]

def save_estado(name, tablero):
    f = open(name, "a", encoding="utf-8") #para las fichas xq sino da error (sin encoding)
    for i in range(8):
        fila_texto = str(i) + "\t" + "\t".join(tablero[i])
        f.write(fila_texto + "\n")
    f.write("\t0\t1\t2\t3\t4\t5\t6\t7\n\n")
    f.close()

name = input("Nombre de la partida: ")
tablero_actual = crear_tablero()
save_estado(name, tablero_actual)

while True:
    accion = input("Introduce mover (m) o terminar (t): ").lower()
    if accion == 't':
        break
    elif accion == 'm':
        try:
            f1 = int(input("Fila origen: "))
            c1 = int(input("Columna origen: "))
            f2 = int(input("Fila destino: "))
            c2 = int(input("Columna destino: "))
            
            pieza_origen = tablero_actual[f1][c1]
            pieza_destino = tablero_actual[f2][c2]
            
            if pieza_origen != " ":
                tablero_actual[f2][c2] = pieza_origen
                tablero_actual[f1][c1] = " "
                save_estado(name, tablero_actual)
                
                if pieza_destino in ["♚", "♔"]: #terminar si es un rey
                    print("¡El Rey ha sido capturado! Fin de la partida.")
                    break
                
                print("Movimiento realizado.")
            else:
                print("Origen vacío.")
        except:
            print("Error en coordenadas.")
