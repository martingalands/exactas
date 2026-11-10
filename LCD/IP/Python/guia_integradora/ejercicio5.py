# Ejercicio 5. Sala de Escape - Promedio de salidas
# Un grupo de amigos apasionados por las salas de escape, esas aventuras inmersivas donde tienen 60 minutos para salir de
# una habitaci´on resolviendo enigmas, llevan un registro meticuloso de todas las salas de escape que hay en Capital. Este registro
# indica si han visitado una sala y si pudieron o no salir de ella. Un 0 significa que no fueron, un 61 que no lograron salir a tiempo,
# y un n´umero entre 1 y 60 representa los minutos que les tom´o escapar exitosamente. Con estos datos, pueden comparar sus
# logros y desaf´ıos en cada nueva aventura que emprenden juntos.
# Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados
# para cada sala de escape en Capital, escribir una funci´on en Python que devuelva un diccionario. En este nuevo diccionario,
# las claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la cantidad de salas de las que cada
# persona logr´o salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir).

# problema promedio de salidas (in registro: dict<str, seq⟨Z⟩>) : dict<str, <Z×R>> {
# requiere: {registro tiene por lo menos un integrante.}
# requiere: {Todos los integrantes de registro tiene por lo menos un tiempo.}
# requiere: {Todos los valores de registro tiene la misma longitud.}
# requiere: {Todos los tiempos de los valores de registro est´an entre 0 y 61 inclusive.}
# asegura: {res tiene las mismas claves que registro.}
# asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a
# 0 y menor estricto a 61 que figuran en sus valores de registro.}
# asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor estricto a 0 y 
# menor estricto a 61 que figuran en sus valores de registro; sino es 0.0.}
# }


def tiempo_mas_rapido (registro:dict[str,list[int]])->dict[str,(int,float)]:

    dict_res : dict[str,(int,float)] = {}
    for integ in registro.keys():
        lista_tiempos_res:list[int] = []
        
        tiempos:int= registro[integ] 
            
        for tiempo in tiempos:
            if tiempo not in [0,61]:
                lista_tiempos_res.append(tiempo)

        if len(lista_tiempos_res)>0:
            dict_res[integ] = (len(lista_tiempos_res),promedio(lista_tiempos_res))
        else:
            dict_res[integ] = (len(lista_tiempos_res),0.0)
    return dict_res


registro = {"martin":[29,31,0,61],"laura":[15,55,0,55]}


def promedio(lista:list[int])->float:
    suma:int = 0
    for elem in lista:
        suma += elem
    promedio:float= suma/len(lista)

    return promedio


print(tiempo_mas_rapido(registro))