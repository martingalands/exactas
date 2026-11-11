from random import shuffle
from queue import Queue as Cola


#armar secuencia de bingo
carton = [12,4,5,9,8]
bolillero = Cola()
for i in range(99):
    bolillero.put(i)

def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int])->int:
    tachados = 0
    contador = 0
    while tachados<12:
        bolilla = bolillero.get()
        contador += 1
        if bolilla in carton:
            tachados += 1
    return contador


print(jugar_carton_de_bingo(carton,bolillero))