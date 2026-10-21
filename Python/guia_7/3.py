from ejercicio1 import ordenados


#def pertenece_a_cada_uno_version_1(s:list,e:int,)



def ordenados(s:list[int])->bool:
    res: bool = True
    for i in range(len(s)-1):
        if s[i]<s[i+1]:
            res = True and res
        else:
            return False
    #si no entró al condicional entonces tiene que ser False
    return res



def es_matriz(s:list[list[int]])->bool:
    if len(s)>0:
        for i in range(len(s)-1):
            if len(s[i])>0 and len(s[i+1])==len(s[i]):
                return True
    else:
        return False

#print(es_matriz([[1,1,1],[2,2,2],[3,3,3]]))


def columna(m:list[list[int]],c:int)->list[int]:
    res : list = []
    if es_matriz(m):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if j == c:
                    res.append(m[i][c]) 
    return res

#print(columna([[1,2,3],[4,5,6],[7,8,9]],0))



def columnas_ordenadas(m:list[list[int]])->list[bool]:
    res : list[bool] = []
    if es_matriz(m):
        for c in range(len(m)):
            res.append(ordenados(columna(m,c)))
    return res


#print(columnas_ordenadas([[1,2,3],[2,5,6],[7,8,9]]))



def filas_ordenadas(m:list[list[int]])->bool:
    res: bool = True
    for i in range(len(m)):
        if ordenados(m[i])==True:
            res = res and True
        else:
            res = res and False

    return res

#print(filas_ordenadas([[1,2,3],[1,2,3],[1,2,3]]))


def fila(m:list[list[int]],c:int)->list[int]:
    if es_matriz(m):
        for i in range(len(m)):
            if i == c:
                return m[c]
            

#print(fila([[1,2,3],[1,153,3],[1,2,4131]],2))




def trasponer(m:list[list[int]])->list[list[int]]:
    mt: list = []
    if es_matriz(m):
        for i in range(len(m)):
            mt.append(columna(m,i))
        return mt

#print(trasponer([[1,2,3],[4,5,6],[7,8,9]]))