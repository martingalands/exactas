# Ejercicio 15. Hospital - Empleado del mes
# Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es
# una lista de las horas trabajadas por d´ıa, queremos saber quienes trabajaron m´as para darles un premio. Se deber´a buscar la o
# las claves para la cual se tiene el m´aximo valor de cantidad total de horas, y devolverlas en una lista.
# problema empleados del mes (horas:dicc<Z, seq⟨Z⟩) : seq⟨Z⟩ {
# requiere: {No hay valores en horas que sean listas vac´ıas.}
# asegura: {Si ID pertence a res entonces ID pertence a las claves de horas.}
# asegura: {Si ID pertenece a res, la suma de sus valores de horas es el m´aximo de la suma de elementos de horas de todos
# los otros IDs.}
# asegura: {Para todo ID de claves de horas, si la suma de sus valores es el m´aximo de la suma de elementos de horas de
# los otros IDs, entonces ID pertenece a res.}
# }

def empleados_del_mes(dicc:dict[int,list[int]])->list[int]:
    res: list[int] = []
    maximo: int = 0
    dict_horas_empleado: dict[int,int] = {}
    for clave in dicc:
        horas_empleado:int=total_horas(dicc[clave])
        dict_horas_empleado[clave] = horas_empleado

        #busco el maximo
        if horas_empleado>= maximo:
            maximo = horas_empleado

    #ahora que tengo el maximo me quedo solo con aquellos iguales al maximo
    for clave in dict_horas_empleado:
        if dict_horas_empleado[clave] == maximo:
            res.append(clave)

    return res

    

def total_horas(lista:list[int])->int:
    total: int = 0

    for horas_trabajadas in lista:
        total += horas_trabajadas
    return total



print(empleados_del_mes({2624525:[12,11,5,10],543435413:[16,12,18,12],131515:[5,5,10,11],15315313:[16,16,15,11]}))
