# Ejercicio 12. Ta-Te-Ti-Facilito
# Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su
# ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una ”X” en su turno y Beto pone una ”O” en el
# suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. Si el tablero est´a completo y no gan´o nadie,
# entonces se declara un empate. El tablero comienza vac´ıo, representado por ” ” en cada posici´on. Notar que dado que juegan por
# turnos y comienza Ana poniendo una ”X” se cumple que la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad
# de ”X” son uno m´as que la cantidad de ”O”. Se nos pide implementar una funci´on en python quien gano el tateti facilito que
# determine si gan´o alguno, o si Beto hizo trampa (puso una ”O” cuando Ana ya hab´ıa ganado).
# problema quien gano el tateti facilito (in tablero:seq⟨seq⟨Char⟩⟩) : Z {
# requiere: {tablero es una matriz cuadrada.}
# requiere: {5 ≤ |tablero[0]| ≤ 10.}
# requiere: {tablero s´olo tiene ”X”, ”O” y ”” (espacio vac´ıo) como elementos.}
# requiere: {En tablero la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad de ”X” es uno m´as que la
# cantidad de ”O”.}
# asegura: {res = 1 ⇔ hay tres ”X” consecutivas en forma vertical(misma columna) y no hay tres ”O” consecutivas en
# forma vertical(misma columna).}
# asegura: {res = 2 ⇔ hay tres ”O” consecutivas en forma vertical (misma columna) y no hay tres ”X” consecutivas en
# forma vertical(misma columna).}
# asegura: {res = 0 ⇔ no hay tres ”O” ni hay tres ”X” consecutivas en forma vertical.}
# asegura: {res = 3 ⇔ hay tres ”X” y hay tres ”O” consecutivas en forma vertical (evidenciando que beto hizo trampa).}
# }

mat = [["X","X","X","O","O","X"],
       ["X","O","O","O","X","O"],
       ["X","O","X","X","X","X"],
       ["O","X","X","X","O","O"],
       ["O","O","O","X","O","O"],
       ["O","X","O","X","X","X"]]


def check_consistencia_turnos(tablero:list[list[str]])->bool:
    equis: str = 0
    os : str = 0
    for fila in range(len(mat)):
        for columna in range(len(mat[fila])):
            if mat[fila][columna] == "X":
                equis += 1
            elif mat[fila][columna] == "O":
                os += 1
    return equis == os,equis,os

#print(check_consistencia_turnos(mat)[1:])


def columna(m:list[list[str]],c:int)->list[str]:
    res: list[str] = []
    for fila in range(len(m)):
        for columna in range(len(m[fila])):
            if columna == c:
                res.append(m[fila][columna])
    return res


#print(columna(mat,2))

def quien_gano_el_tateti_facilito(tablero:list[list[str]])-> int:
    gana_beto:int =  0
    gana_ana:int = 0
    if check_consistencia_turnos(tablero):
        #agarro cada columna y veo si hay una subsecuencia de XXX o OOO
        for c in range(len(tablero[0])):
            columna_actual = columna(tablero,c)
            #recorro cada elemento de la columna actual para ver si hay una subsecuencia de XXXs u OOOs
            signo_anterior: str = columna_actual[0]
            cadena_acumulada: str = signo_anterior      #el primer elemento de la cadena acumulada es el primer signo
            #arranco en 1 porque el signo del primer lugar ya lo tengo
            for i_signo in range(1,len(columna_actual)):
                signo_actual = columna_actual[i_signo]
                if signo_actual == signo_anterior:
                    
                    cadena_acumulada += signo_actual        #si coincide el signo actual con el anterior entonces lo agrego a la cadena acumulada
                    signo_anterior = signo_actual           #ahora el signo anterior es el ex signo actual
        
                    if "XXX" in cadena_acumulada:
                        gana_ana = 1
                    elif "OOO" in cadena_acumulada:
                        gana_beto = 1
                else:
                    signo_anterior = signo_actual
                    cadena_acumulada = signo_actual     #si el signo actual no es igual al signo anterior, entonces la cadena se rompe y empiezo una nueva con el signo actual
                    
        if gana_ana == 1 and gana_beto == 0:
            res = 1
        elif gana_ana == 0 and gana_beto == 1 :
            res = 2
        elif gana_ana == 1 and gana_beto == 1:
            res = 3
        else:
            res = 0

    return res

print(quien_gano_el_tateti_facilito(mat))



