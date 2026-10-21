


def agrega_a_lista()->list[str]:
    
    lista: list[str] = []
    palabra: str = input()
    while palabra not in ['listo','']:
        lista.append(palabra)
        palabra = input()
    return lista

#print(agrega_a_lista())


def historial_SUBE():
    operacion = input('Seleccione operacion: ')
    saldo: float = 0 
    #historial: tuple(str,float) =
    while operacion in ['C','D','X']:
        if operacion == 'C':
            saldo += float(input('Ingrese saldo a cargar:'))
            print(saldo)
            operacion = input('Seleccione operacion: ')
        elif operacion == 'D':
            saldo -= float(input('Ingrese saldo a debitar'))
            print(saldo)
            operacion = input('Seleccione operacion: ')
        elif operacion == 'X':
            print('Cerrando sesion')
            break


#print(historial_SUBE())

def contiene_minusculas(pword:str)->bool:
    s: int = 0
    for c in pword:
        if c.islower():
            res: bool = True
            return res
        else:
            pass
    res: bool = s >0
    return res


def contiene_mayusculas(pword:str)->bool:
    s: int = 0
    for c in pword:
        if c.isupper():
            s += 1
        else:
            pass
    res: bool = s>0
    return res

def contiene_digito(pword:str)->bool:
    s: int = 0
    for c in pword:
        if c.isdigit():
            s += 1
        else:
            pass
    res: bool = s>0
    return res


def seguridad_contrasenia(pword:str)->str:
    if len(pword)>8 and contiene_mayusculas(pword) and contiene_minusculas(pword):
        return 'VERDE'
    elif len(pword)<8:
        return 'ROJA'
    else:
        return 'AMARILLA'


#print(seguridad_contrasenia('Hojalata3'))



