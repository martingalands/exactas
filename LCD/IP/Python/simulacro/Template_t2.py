from queue import LifoQueue as Pila


# Ejercicio 1
def ejercicio1(s: list[int], n: int) -> list[int]:
    res:list[int] = []
    for i in range(len(s)):
        suma_parcial: int = 0
        #j:int = i
        res_candidata : list[int] = []
        # while suma_parcial <= n:
        #     suma_parcial += s[j]
        #     res_candidata.append(s[j])
        #     j += 1
        for j in range(i,len(s)):
            if suma_parcial == n:
                res: list[int] = res_candidata
            else:
                suma_parcial += s[j]
                res_candidata.append(s[j])
    return res
    


# Ejercicio 2
def ejercicio2(examenes: Pila[(str, int)]) -> Pila[str]:
    
    #en res van los nombres de los que tienen tema 1
    #en examenes va la tupla original que tiene tema 2 (se modifica la pila)
    
    res : Pila = Pila()
    lista_res:list[str] = []  #con esto apilo los nombres luego
    lista_examenes: list[tuple[str,int]] = []  #con esto apilo tuplas de examenes tema 2 luego
    while not examenes.empty():
        tupla_actual: tuple[str,int] = examenes.get()
        tema: int = tupla_actual[1]
        nombre: str = tupla_actual[0]
        if tema==1:
            lista_res.insert(0,nombre)  #insert me permite poner al principio
        else:
            lista_examenes.insert(0,tupla_actual) #insert me permite poner al principio

    for i in range(len(lista_examenes)):
        examenes.put(lista_examenes[i])

    for j in range(len(lista_res)):
        res.put(lista_res[j])

    print(lista_examenes)
    print(lista_res)
    return res


# Ejercicio 3
def ejercicio3(A: list[list[int]]) -> None:
    


# Ejercicio 4
def ejercicio4(eleccion1: dict[str, str], eleccion2: dict[str, str]) -> dict[str, int]:
    # TODO: Implementar
    pass
