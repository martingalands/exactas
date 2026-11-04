# Ejercicio 3


def minimo_de_lista(lista: list[int])->int:
    minimo : int = 0
    for i in range(len(lista)):
        if i == 0:
            minimo = lista[i]
        else:
            if minimo < lista[i]:
                pass
            else:
                minimo = lista[i]
    return minimo


def ejercicio3(A: list[list[int]]) -> None:
    #el out sale con len(A) +1
    #la matriz A de entrada es igual a la matriz A de salida.
    #j no llega hasta la ultima columna
    #la ultima columna vale minimoDeLista(A@pre fila i) para todo i en ese rango. o sea que le pongo el minimo valor de la fila

    for fila in range(len(A)):
        #A_fila_copia: list[int] = A[fila].copy()
        #contador :int = 0
        #for columna in range(len(A[fila])-1):
        #    contador += 1
        #A[fila][contador] = minimo_de_lista(A_fila_copia)
        A[fila].append(minimo_de_lista(A[fila]))


matriz = [[1,2,3],
 [0,0,1],
 [5,1,9]]

ejercicio3(matriz)
print(matriz)




#print(minimo_de_lista([-64,0,23,6,-25]))

