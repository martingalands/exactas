
def secuencia_mas_larga_num_consec(s:list[int])->int:
    longitud_maxima = 0
    longitud_actual = 0
    indice_maximo = 0
    indice_actual = 0
    for i in range(len(s)):
        numero_actual = s[i]
        if numero_actual > 0:   #condicion
            
            if longitud_actual == 0:    #reinicio el indice si estoy en el primer paso o bien, si el paso anterior no sumó a la longitud (no cumplió condicion)
                indice_actual = i

            longitud_actual += 1        #sumo esto despues del primer if porque forma parte de la condicion. 

            if longitud_actual > longitud_maxima:   #luego de aumentar la longitud actual me fijo si superé lo mejor que tenia. si se cumple tengo que actualizar ambas variables.
                indice_maximo = indice_actual       # siempre que me mueva en la lista, el indice de la mejor subsecuencia va a ser i (si era 0 con un elemento, entonces si lo supere en indice 1, será con dos)
                longitud_maxima = longitud_actual
        else:
            longitud_actual = 0

    return indice_maximo


print(secuencia_mas_larga_num_consec([-2, 3, 5, -1, 8, 9, 10, -4]))
#print(secuencia_mas_larga_num_consec([2, 3, 5, -1, 8, 9, 10, -4]))