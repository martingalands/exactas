def imprimir_saludo(nombre: str) -> str:
    print(f'Hola {nombre}')


#imprimir_saludo('Martin')


from math import sqrt

def raiz_cuadrada_de(numero: int) ->float:
    res: float = sqrt(numero)
    return res


#print(raiz_cuadrada_de(5))


def fahrenheit_a_celsius(temp_far: float)->float:
    res: float = (temp_far-32) *5/9
    return res


#print(fahrenheit_a_celsius(100))


def imprimir_dos_veces(estribillo: str)->str:
    res : str = (estribillo+'\n')*2
    print(res)

#imprimir_dos_veces('personalmente creo que todo esto es una locura')




def es_multiplo_de(n: int, m: int) -> bool:
    if m == 0:
        return None
    else:
        k: int = n
        while k > 0:
            res: bool = n == k * m
            if res == True:
                return res    #<-----si esto no se define entonces se define al final
            else:
                k -= 1

        return False



#print(es_multiplo_de(60,2))

def es_par(numero:int)->bool:
    res: bool = es_multiplo_de(numero,2)== True
    return res

#print(es_par(25))

def cantidad_de_pizzas(comensales:int,min_cant_de_porciones:int)->int:
    cantidad_total: int= comensales*min_cant_de_porciones
    if es_multiplo_de(cantidad_total,8):
        res : int = (cantidad_total)/8
        return res
    else:
        res: int = parte_entera(cantidad_total/8) #o usar round
        return res


#si tengo 3 comensales y cada uno come 3 porciones, entonces, como 8/3 < 3*3 = > cantidad_de_pizzas = 3*3-8+1


def parte_entera(x:float)->int:
    if x < 1:
        res: int = 0
    else:
        res: int = 1 + parte_entera (x-1)
    return res


#print(cantidad_de_pizzas(4,5),'pizzas')




