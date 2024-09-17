from random import randint
def crea_matriz(filas:int, columnas:int, lim_inf:int, lim_sup:int):
    Lista = []
    for i in range(filas):
        Lista.append([])
        for j in range(columnas):
            n = randint(lim_inf, lim_sup)
            Lista[i].append(n)
    return Lista

def imprime_matriz(Lista):
    filas = len(Lista)
    columnas = len(Lista[0])
    for f in range(filas):
        print ('|', end= ' ')
        for c in range(columnas):
            print(f"{Lista[f][c]:^5}|", end=' ')
        print()

Matriz = crea_matriz(5, 12, 31, 191)
imprime_matriz(Matriz)