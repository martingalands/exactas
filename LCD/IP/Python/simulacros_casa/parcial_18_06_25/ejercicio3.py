def intercambiar_e_invertir_columnas(A:list[list[int]],col1:int,col2:int):
    A_t : list[list[int]]  = []  #queda la traspuesta de A
    for columna in range(len(A[0])):
        if columna == col1:
            A_t.insert(col2,invierte_columna(obtiene_columna(A,columna)))
        elif columna == col2:
            A_t.insert(col1,invierte_columna(obtiene_columna(A,columna)))
        else:
            A_t.append(obtiene_columna(A,columna))

    #truquito para conservar referencia:
    A_nueva: list[list[int]] = traspone(A_t)
    
    A.clear()  #limpio todo lo que tenga la lista y la recreo, pero manteniendo la direccion de memoria
    for fila in A_nueva:
        A.append(fila)




# la matriz queda igual excepto en las columnas que se intercambian
# intercambio columnas e invierto la posicion de fila




mat = [[1,2,3],
       [40,50,60],
       [-7,-8,-9]]


# mat2 = [[1, -9, -8],
#         [40, 60, 50],
#         [-7, 3, 2]]

mat3 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

def obtiene_columna(A:list[list[int]],col:int)->list[int]:
    res: list[int] = []
    for fila in range(len(A)):
        for columna in range(len(A[fila])):
            if columna == col:
                res.append(A[fila][col])
    return res



def traspone(A:list[list[int]]):
    A_t: list[list[int]] = []
    for fila in range(len(A)):
        A_t.append(obtiene_columna(A,fila))
    return A_t



def invierte_columna(columna:list[int])->list[int]:
    res: list[int] = []
    for fila in range(len(columna)):
        res.insert(0,columna[fila])
    return res


print(id(mat))

intercambiar_e_invertir_columnas(mat,1,2)
print(mat)  #veo la variable mat (se tuvo que haber modificado)

print(id(mat))

#puedo chequear que la direccion en memoria es la misma