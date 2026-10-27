def calcular_promedio_por_estudiante(notas:list[(str,float)])->dict:
    dict_notas = {}
    for elemento in notas:
        nombre_alumno = elemento[0]
        nota = elemento[1]
        if not nombre_alumno in dict_notas.keys():
            dict_notas[nombre_alumno] = [nota]
        else:
            dict_notas[nombre_alumno].append(nota)

    dict_notas_final: dict[str,list[int]] = {}
    for nombre in dict_notas.keys():
        notas_de_alumno = dict_notas[nombre]
        dict_notas_final[nombre] = promedio(notas_de_alumno)
    return dict_notas_final
    
        
def promedio(notas_de_alumno:list[int])->float:
    suma_notas: float = 0
    longitud: int = 0
    longitud = len(notas_de_alumno)
    for valor_nota in notas_de_alumno:
        suma_notas += valor_nota
    return suma_notas/longitud

#print(promedio([10,10,10,10]))
print(calcular_promedio_por_estudiante([("pedro",5),("pedro",10),("luis",5)]))


    

#print(calcular_promedio_por_estudiante(""))



