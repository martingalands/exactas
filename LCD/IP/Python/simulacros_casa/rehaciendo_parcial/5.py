# Ejercicio 5 [2 puntos]
# Implementar la función ejercicio5:

# problema ejercicio5 (inout A: seq⟨seq⟨Z⟩⟩) {
#   requiere: { |A| > 0 }
#   requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
#   requiere: { Todos los elementos de A son distintos entre sí }
#   modifica: { A }
#   asegura: { A tiene exactamente las mismas dimensiones que A@pre }
#   asegura: { Sea max el máximo elemento de A@pre y sea min el mínimo elemento de A@pre. Sea fmax la fila tal que existe una columna j con A@pre[fmax][j] = max, y sea fmin la fila tal que existe una columna j con A@pre[fmin][j] = min. Entonces A[fmax][k] = A@pre[fmin][k] y A[fmin][k] = A@pre[fmax][k] para todo k en rango }
#   asegura: { Con fmax y fmin definidas como arriba, A[f][k] = A@pre[f][k] para todo f en rango tal que f ≠ fmax y f ≠ fmin, y todo k en rango }
# }



def ejercicio5(A:list[list[int]]):

    nf_min:int = 0
    nf_max:int = 0

    minimo:int = A[0][0]
    maximo:int = A[0][0]

    fila_maximo:list[int] = []
    fila_minimo:list[int] = []

    #ubico el maximo y el minimo y en que fila estan, ademas de guardar la fila entera
    for fila in range(len(A)):
        for columna in range(len(A[0])):
            valor:int =  A[fila][columna]
            if valor > maximo:
                maximo = valor
                nf_max = fila
                fila_maximo = A[fila]
            elif valor < minimo:
                minimo = valor
                nf_min = fila
                fila_minimo = A[fila]
    
    #como paso por referencia tengo que hacer una copia del original y rearmar
    A_copia = A.copy()
    A.clear()

    print(minimo)
    print(maximo)
    print(nf_max)
    print(nf_min)

    print(fila_minimo)


    for nfila in range(len(A_copia)):
        if nfila == nf_min:
            A.append(A_copia[nf_max])
        elif nfila == nf_max:
            A.append(A_copia[nf_min])
        else:
            A.append(A_copia[nfila])
        



# mat = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]

mat = [[1,-1,2],[3,4,-5],[9,8,7]]


ejercicio5(mat)

print(mat)