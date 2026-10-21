#2kg/cm --> 200kg/m
#3kg/cm --> 300kg/m




def peso_pino(altura:float)->float:
    DENS_3 = 300
    DENS_2 = 200
    # if altura<3: #en metros
    #     res: float = altura*DENS_3
    #     return res
    # else:
    #     res: float = (altura-3)*DENS_2+(altura-2)*DENS_3
    #     return res
    res: float = min(altura,3) * DENS_3 + max(altura-3,0) * DENS_2
    
    #con min veo si supere los 3 metros.
    #las funciones max y min elijen al mas grande o mas chico entre dos numeros
    #entonces min (5,3) elije a 3, entonces multiplico a 3 por la densidad de 3 metros
    #y como max(5-3,0) da 2, entonces multiplico 2 por la densidad y solo le sumo esos dos metros
    return res



print(peso_pino(5))

def es_peso_util(peso:float)->bool:
    res: bool = peso>= 400 and peso <= 1000
    return res


#print(es_peso_util(800))


def sirve_pino(altura)->bool:
    res: bool = es_peso_util(peso_pino(altura))
    return res

print(sirve_pino(3))