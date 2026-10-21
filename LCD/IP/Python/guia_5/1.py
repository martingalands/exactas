print('¡Hola Mundo!')



def imprimir_un_verso():
    print("""Quiero vivir aquí, mas quiero cambiar \n
    Cambiar para sentirme vivo \n
    Y te daré una flor \n
    Antes que un decadrón \n
    Oh, mi amor, estoy tranquilo pero herido""")


imprimir_un_verso()



def raizDe2() -> float:
    raiz: float = round(2 ** (1/2),4)
    return raiz


print(raizDe2())



def factorial_de_dos() -> int: 
    res: int = 2*1*1
    return res


print(factorial_de_dos())


import math

def perimetro()->float:
    res: float = 2*math.pi
    return res


print(perimetro())


