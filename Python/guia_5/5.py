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



def es_par(numero:int)->bool:
    res: bool = es_multiplo_de(numero,2)== True
    return res


def doble_si_es_par(numero:int)->int:
    if es_par(numero):
        res : int = numero * 2
        return res
    else:
        return numero


#print(doble_si_es_par(10))

#-----------------------------------------------------------------------------------------

#si numero no es par, devuelvo 2*(numero+1)

#requiere: n perte z
#asegura: res perte z
#asegura: res = n si z es par o res = 2*(n+1)
def devolver_valor_si_es_par_si_no_el_que_sigue(numero:int)->int:
    if es_par(numero):
        res: int = numero
        return res
    else:
        res: int = 2*(numero+1)
        return res


#print(devolver_valor_si_es_par_si_no_el_que_sigue(5))


#??


#-----------------------------------------------------------------------------------------

def  doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int)->int:
    if es_multiplo_de(numero,3) and es_multiplo_de(numero,2):
        res: int = numero*2*3
        return res
    else:
        res: int = numero*3
        return res

# def  doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int)->int:
#     if es_multiplo_de(numero,3):
#         res: int = numero*2
#         return res
#     else:
#         res: int = numero*3
#         return res



#print(doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))


#-----------------------------------------------------------------------------------------

def lindo_nombre(nombre:str)->bool:
    if len(nombre)>=5:
        res: str= 'Tu nombre tiene muchas letras!'
        return res
    else:
        res: str= 'Tu nombre tiene menos de 5 caracteres'
        return res

#print(lindo_nombre('martin'))

def elRango(numero:int)->str:
    if numero <= 20:
        if numero>= 5 and numero<=20:
            print('entre 5 y 20')
        else:
            print('menor a 5')
    else:
        print('mayor a 20')

    
#elRango(3)


#-----------------------------------------------------------------------------------------

def trabajo_o_vacaciones(edad:int,sexo:str)->str:
    if  edad <= 65:
        if edad <18:
            print('Andá de vacaciones')
        else:
            if sexo == 'F' and edad>=60:
                print('Andá de vacaciones')
            else:
                print('Te toca trabajar')
    else:
        print('Andá de vacaciones')


#trabajo_o_vacaciones(66,'F')


#-----------------------------------------------------------------------------------------


def prod1():
    i: int = 1
    numero: int = 10
    while i<=numero:
        print(i)
        i = i+1

#prod1()

def prod2():
    i: int = 10
    numero: int = 40
    while i<=numero:
        if es_par(i):
            print(i)
            i = i+1
        else:
            i = i+1
            continue

#prod2()

def prod3():
    i: int = 0
    while i<=10:
        print('eco')
        i = i+1

#prod3()

def prod4(t_minus:int):
    i: int = t_minus
    while i>=1:
        print(i)
        i = i-1
    print('Despegue')

#prod4(10)


def viaje(dep:int,arr:int):
    i: int = dep
    while i>=arr :
        print(f'Viajó un año al pasado, estamos en el año: {i}')
        i = i-1

#viaje(2026,2001)


def viaje_aristoteles(dep:int,arr:int):
    i: int = dep
    while i>(arr-20):
        if i-arr<20:
            print(f'Viajo 20 años al pasado, estamos en el año: {i}')
            break
        else:
            print(f'Viajó 20 años al pasado, estamos en el año: {i}')
            i = i-20

#viaje_aristoteles(2026,384)



