# Ejercicio 4

#dict_prueba_1 = {}
#dict_prueba_1 = {}

def ejercicio4(eleccion1: dict[str, str], eleccion2: dict[str, str]) -> dict[str, int]:
    #si el candidato fue votado en ambas elecciones por la misma persona, entonces aparece en res
    #sumo la cantidad de ciudadanos que volvieron a votar al mismo candidato
    res: dict[str,int] = {} #diccionario con candidato como key y la suma de los votos mantenidos como value
    for ciudadano in eleccion1.keys():
        candidato: str = eleccion1[ciudadano]
        if candidato == eleccion2[ciudadano]:
            if candidato in res.keys():
                res[candidato] += 1
            else:
                res[candidato] = 1
    return res    



print(ejercicio4 ({"Ana":"X","Beto":"Y","Caro":"X"} ,{"Ana":"X","Beto":"X","Caro":"X"}))