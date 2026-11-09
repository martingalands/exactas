def es_primo(numero:int)->bool:
    j = numero-1
    res: bool = True
    while j > 1:
        if numero % j == 0:
            res = False
        j -= 1
    return res


#print(es_primo(2))

def obtiene_3_cifras(numero:int)->int:
    res: int = numero % 1000
    return res


def filtrar_codigos_primos(codigos_barra:list[int])->list[int]:
    res: list[int] = []
    for cod in codigos_barra:
        cifras_codigo_actual = es_primo(obtiene_3_cifras(cod))
        if cifras_codigo_actual:
            res.append(cod)
    return res


#print(filtrar_codigos_primos([2,3,5,101,130,103,107,4004]))