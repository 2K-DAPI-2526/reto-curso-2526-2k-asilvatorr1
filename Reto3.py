muro = ((0,2), (0,3), (0,4), (0,5), (0,6),
        (1,0), (1,2), (1,3), (1,4), (1,5), (1,6),
        (2,0), (2,5), (2,6),(3,0), (3,1), (3,2), 
        (3,3), (3,5), (3,6),
        (4,0), (4,5), (4,6),(5,0), (5,3),
        (6,0), (6,1), (6,2), (6,3), (6,4), (6,5))

laberinto = []
for i in range(7):
    fila = []
    for j in range(7):
        if (i, j) in muro:
            fila.append('X')
        elif i == 6 and j == 6:
            fila.append('S')
        else:
            fila.append(' ')
    laberinto.append(fila)

for fila in laberinto:
    print(fila)



#tarea 2
def buscar(r, c, lab, camino, visitados):
    if r == 4 and c == 4:
        return camino

    visitados.append((r, c))

    movimientos = [(1, 0, 'Abajo'), (0, 1, 'Derecha'), (-1, 0, 'Arriba'), (0, -1, 'Izquierda')]

    for dr, dc, direccion in movimientos:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < 5 and 0 <= nc < 5:
            if lab[nr][nc] != 'X' and (nr, nc) not in visitados:
                resultado = buscar(nr, nc, lab, camino + [direccion], visitados)
                if resultado:
                    return resultado

    visitados.pop()
    return None

solucion = buscar(0, 0, laberinto, [], [])
print(solucion)
