


#no hace falta usar listas ni dobles for.
#cada variable responde a una pregunta: cuantos tengo ahora, donde comence? que tengo como mejor resultado?


def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    long_max: int = 0
    indice_max: int = 0
    long_actual: int = 0
    indice_actual: int = 0

    for i in range(len(tipos_pacientes_atendidos)):
        if (tipos_pacientes_atendidos[i] == "perro"
            or tipos_pacientes_atendidos[i] == "gato"):

            if long_actual == 0:   #cuantos voy?
                indice_actual = i 

            long_actual += 1

            if long_actual > long_max:  #si se cumple que lo que llevo es mas que lo que habia antes actualizo el resulado (indice y longitud maximas con lo que llevo actualmente)
                long_max = long_actual
                indice_max = indice_actual

        else:
            long_actual = 0            #reinicio el contador de longitud actual

    return indice_max


print(subsecuencia_mas_larga(["perro","hamster","hamster","perro","gato","hamster","gato"]))


