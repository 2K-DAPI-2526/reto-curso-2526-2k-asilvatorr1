#parte 2
def mostrar_movimiento():
    name = input("Nombre de la partida: ")
    try:
        f = open(name, "r", encoding="utf-8") #para las fichas
        lineas = f.readlines()
        f.close()
        
        tableros = []
        for i in range(0, len(lineas), 10):
            bloque = lineas[i : i+9]
            if bloque:
                tableros.append(bloque)
        
        n = int(input(f"Movimiento (0-{len(tableros)-1}): "))
        
        if 0 <= n < len(tableros):
            for fila in tableros:
                print(fila.replace("\t", "  ").strip("\n"))
        else:
            print("No existe.")
            
    except FileNotFoundError:
        print("Error archivo.")

mostrar_movimiento()
