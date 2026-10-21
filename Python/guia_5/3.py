def alguno_es_0(numero1:float,numero2:float)->bool:
    res: bool = numero1==0 or numero2==0
    return res


#print(alguno_es_0(5,2/5))

def ambos_son_0(numero1:float,numero2:float)->bool:
    res: bool = numero1==0 and numero2==0
    return res

#print(ambos_son_0(1,0))


def es_nombre_largo (nombre: str) ->bool:
    if len(nombre)>= 3 and len(nombre) <= 8:
        res: bool= True
        return res
    else:
        res: bool = False
        return res


#print(es_nombre_largo('hholaffmfaf'))


def es_bisiesto(año:int)->bool:
    if es_multiplo_de(año ,100) or (es_multiplo_de(año,4) and not (es_multiplo_de(año,100))):
        res: bool = True
        return res
    else:
        res: bool = False
        return res

#print(es_bisiesto(2060))


