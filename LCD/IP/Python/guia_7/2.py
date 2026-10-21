def sin_vocales(s:list)->list:
    vocales = ['a','e','i','o','u']
    res : str = ''
    for l in range(len(s)):
        if s[l] not in vocales:
            res += s[l]
        else:
            pass
    return res
            

prueba = ["h","o","l","a"]
print(sin_vocales(prueba))



def reemplaza_vocales(s:list)->list:
    sn : str = ''
    vocales = ['a','e','i','o','u']
    for i in range(len(s)):
        if s[i] in vocales:
            sn += '_'
        else:
            sn += s[i]
    return sn


print(reemplaza_vocales("hola"))


def promedio(lista:list[int])->float:
    res: float = 0
    s: int = 0
    if len(lista)>0:
        for i in lista:
            s += i
    res = s/len(lista)
    return res

#print(promedio([10,10,10]))

def menor_4(lista:list[int])->bool:
    res: bool =  True
    for l in lista:
        if l<4:
            res = res and True
        else:
            res = res and False
    return res

def resultado_materia(notas:list[int])->int:
    m4: bool = menor_4(notas)
    pn: float = promedio(notas)
    if m4 or pn<4:
        res : int = 3
        return res
    elif m4 is False and (4 <= pn<7):
        res: int = 2
        return res
    else:
        res: int = 1
        return res


print(resultado_materia([4,10,5,9,8,7,8,7,8,6,5]))
#print(promedio([4,10,5,9,8,7,8,7,8,6,6]))