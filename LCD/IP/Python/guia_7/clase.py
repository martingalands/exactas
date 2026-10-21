#no importa la cardinalidad. usar lower.

vocales = ['a','e','i','o','u']
def vocales_distintas(s:str)->bool:
    lista: list = []
    s = s.lower()
    for i in s:
        if i in vocales:
            lista.append(i)
        else:
            pass
    cont = len(set(lista))
    if cont >= 3:
        return True
    else:
        return False


#print(vocales_distintas('hormigA'))




#[1,2,3,1,5,6,7,8]

# def pos_secuencia_ordenada_mas_larga(s:list)->int:
#     #cand: list
#     cand = []
#     pos = 0
#     for i in range(len(s)):
#         if s[i] < s[i+1]:
#             pos = i
#             if len(cand) < 
#             cand.append(s[i])
#         else:
#             pass


def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    subsecuencias_posibles: list[list[int]] = []
    posiciones_subsecuencias_posibles: list[int] = [0]
    subsecuencia_actual = [s[0]]

    for i in range(len(s) - 1):
        elemento_actual: int = s[i]
        elemento_siguiente: int = s[i + 1]

        if elemento_siguiente >= elemento_actual:
            subsecuencia_actual.append(elemento_siguiente)
        else:
            posiciones_subsecuencias_posibles.append(i + 1)
            subsecuencias_posibles.append(subsecuencia_actual)

            # Reseteo la subsecuencia
            subsecuencia_actual = [elemento_siguiente]

    # Agrego la última subsecuencia
    subsecuencias_posibles.append(subsecuencia_actual)

    indice_subsec_mayor = 0

    for i in range(1, len(subsecuencias_posibles)):
        if len(subsecuencias_posibles[i]) > len(subsecuencias_posibles[indice_subsec_mayor]):
            indice_subsec_mayor = i

    return posiciones_subsecuencias_posibles[indice_subsec_mayor]



#print(pos_secuencia_ordenada_mas_larga([3,4,5,1,2,3,4]))


m = [[1,2,3],[4,5,6],[7,8,9]]



#dos elementos consecutivos pueden ser iguales, el siguiente no puede ser menor que el anterior
#encuentro una secuencia ordenada. guardo la posicion.
#si la secuencia es ordenada y tiene mayor longitud que la guardada reemplazo la lista y el valor de posicion


#[1,2,3,4,1,2,5,6,2]



def columna(m:list[list[int]],c:int)->list[int]:
    res : list = []
    if es_matriz(m):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if j == c:
                    res.append(m[i][c]) 
    return res



def trasponer(m:list[list[int]])->list[list[int]]:
    mt: list = []
    if es_matriz(m):
        for i in range(len(m)):
            mt.append(columna(m,i))

        return mt



def es_matriz(s:list[list[int]])->bool:
    if len(s)>0:
        for i in range(len(s)-1):
            if len(s[i])>0 and len(s[i+1])==len(s[i]):
                return True
            else:
                return False
    else:
        return False


print(trasponer(m))