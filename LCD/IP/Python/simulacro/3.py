# Ejercicio 3
#def ejercicio3(A: list[list[int]]) -> None:
    #el out sale con len(A) +1
    #la matriz A de entrada es igual a la matriz A de salida.
    #j no llega hasta la ultima columna
    #la ultima columna vale minimoDeLista(A@pre fila i) para todo i en ese rango. o sea que le pongo el minimo valor de la fila


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


print(minimo_de_lista([-64,0,23,6,-25]))
