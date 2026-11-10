# Ejercicio 1 (2,25 puntos)
# Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

# problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
#   requiere: { La longitud de v es distinto de 0 }
#   asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
# }

# problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
#   asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia es igual a 1 }
# }


def todos_consecutivos(v: list[int])-> bool:
    res: bool = False
    for i in range(len(v)):
        actual : int = v[i]
        anterior: int = v[i-1]
        if i==0:
            res = True
        elif actual-anterior==1:
            res = True
        else:
            return False
    return res



def subsecuencia_mas_larga(v:list[int])->tuple[int,int]:
    
    long_max: int = 1 #siempre arranco teniendo al menos un elemento
    inicio_max: int = 0 #arranco desde el cero
    res: tuple[int,int] = ()
    
    for i in range(len(v)):
        subsecuencia_cand : list[int] = []  #arranco con lista vacia

        for j in range(i,len(v)): #tengo que arrancar desde el indice donde empiezo a barrer, por eso "i"
            subsecuencia_cand.append(v[j])  #agrego el valor actual. tambien se cumple en el caso del primer valor (range incluye el primer borde). voy agregando de a uno

            if todos_consecutivos(subsecuencia_cand):
                if len(subsecuencia_cand)>long_max:   #si lo que tengo es mas grande que lo que tenia, actualizo el res
                    inicio_max = i
                    long_max = len(subsecuencia_cand)
                    res = (long_max,inicio_max)

    return res



print(subsecuencia_mas_larga([1,2,3,1,1,2,3,4,5,6]))
#print(subsecuencia_mas_larga([1,2,3,4,5,6]))


#print(todos_consecutivos([2]))



#con listas!!!!

# def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
#     subsecuencias_posibles: list[list[int]] = []
#     posiciones_subsecuencias_posibles: list[int] = [0]        #inicializo con la primera posicion de la lista. luego van a agregarse otras
#     subsecuencia_actual = [s[0]]          #inicializo con la primera de la lista. luego va a ser modificada.

#     for i in range(len(s) - 1):           #arranco con el primer elemento de la lista s.
#         elemento_actual: int = s[i]
#         elemento_siguiente: int = s[i + 1]

#         if elemento_siguiente >= elemento_actual:         
#             subsecuencia_actual.append(elemento_siguiente)        #perfecto, agrego el elemento a la lista candidata.
#         else:
#             posiciones_subsecuencias_posibles.append(i + 1)       #agrego la subsecuencia a la lista de posiciones
#             subsecuencias_posibles.append(subsecuencia_actual)    #agrego la subsecuencia a la lista de listas

#             # Reseteo la subsecuencia
#             subsecuencia_actual = [elemento_siguiente]            #reseteo la subsecuencia actual ingresando el proximo elemento de la lista. por ahora queda una lista de un solo elemento

#     # Agrego la última subsecuencia
#     subsecuencias_posibles.append(subsecuencia_actual)            #por cuestiones de borde

#     indice_subsec_mayor = 0                                       #necesito el indice de la subsecuencia de mayor longitud. si necesito quedarme con la primera, puedo meter la condicion en el for de abajo

#     for i in range(1, len(subsecuencias_posibles)):
#         if len(subsecuencias_posibles[i]) > len(subsecuencias_posibles[indice_subsec_mayor]):
#             indice_subsec_mayor = i

#     return posiciones_subsecuencias_posibles[indice_subsec_mayor]