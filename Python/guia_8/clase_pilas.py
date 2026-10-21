from queue import LifoQueue as Pila, Queue as Cola

p = Pila()

# con put agrego
# con get obtengo y desapilo
# con empty veo si esta vacia
# con p.queue veo todos los elementos


c = Cola()




#---------------------------------------------------------
import random


def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
    res: Pila[int] = Pila()
    for i in range(cantidad):
        aleat: int = random.randint(desde,hasta)
        res.put(aleat)
    return res

var = generar_nros_al_azar(50,1,100)

#print(var.queue)
#print(var.get())


#print(pila.queue)

def buscar_el_maximo(p:Pila[int])->int:
    val: int = 0
    lista: list[int] = []
    lista.append(p.get())
    while not p.empty():
        lista.append(p.get())
        if lista[0] >= lista[1]:
            lista[0] = lista[0]
        else:
            lista[0] = lista[1]
        lista.pop(1)
    return lista[0]

#version de la clase
# def buscar_el_maximo(p:Pila)->int:
#     assert not p.empty()
#     maximo: int = p.get()
#     while not p.empty():
#         x = p.get()
#         if maximo < x:
#             maximo = x
#     return maximo

p = Pila()
p.put(1)
p.put(50)
p.put(2)

print(buscar_el_maximo(p))


#def armar_secuencia_bingo()->Cola:



from random import shuffle

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