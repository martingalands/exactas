# Ejercicio 8. Sala de Escape - Escape en solitario
# Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los
# tiempos (en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un n´umero entre 1 y 60 si salieron), escribir
# una funci´on en Python que devuelva los ´ındices de todas las filas (que representan las salas) en las cuales el primer, segundo y
# cuarto amigo no fueron (0), pero el tercero s´ı fue independientemente de si sali´o o no).
# problema escape en solitario (in amigos por salas: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
# requiere: {Hay por lo menos una sala en amigos por salas.}
# requiere: {Hay 4 amigos en amigos por salas.}
# requiere: {Todos los tiempos en cada sala de amigos por salas est´an entre 0 y 61 inclusive.}
# asegura: {La longitud de res es menor igual que la longitud de amigos por salas.}
# asegura: {Por cada sala en amigos por salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de
# 0, la posici´on de dicha sala en amigos por salas debe aparecer res.}
# asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos por salas[i] es 0, y
# el tercer valor es distinto de 0.}
# }


mat = [[0,0,0,0],[6,0,60,52],[4,5,19,32],[56,23,48,57]]

def escape_en_solitario(amigos_por_salas:list[list[int]])->list[int]:
    res:list[list[int]] = []
    for s in range(len(amigos_por_salas)):
        sala:list[int] = amigos_por_salas[s]
        booleano: bool = True
        for a in range(len(sala)):
            if a in [0,1,3] and sala[a] == 0:
                booleano = booleano and True
            elif (a in [0,1,3] and sala[a] != 0) or (a == 2 and sala[a] == 0):
                booleano = booleano and False
        if booleano:
            res.append(s)
    return res


print(escape_en_solitario(mat))