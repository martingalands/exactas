from queue import Queue as Cola
from random import randint

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int)->Cola[int]:
    num: int = randint(desde,hasta)
    res: Cola = Cola()
    res.put(num)
    return res







