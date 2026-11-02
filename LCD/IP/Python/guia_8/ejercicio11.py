from queue import Queue as Cola

cola_prueba: Cola = Cola()

cola_prueba.put(("martin",10))
cola_prueba.put(("agustin",9))
cola_prueba.put(("agustina",2))

def buscar_nota_minima(c:Cola)->int:
    while not c.empty():
        minimo: int = 10
        tupla_actual: tuple(str,int) = cola_prueba.get()
        #print(tupla_actual[0])
        nota_actual: int = tupla_actual[1]
        if nota_actual < minimo:
            minimo = nota_actual
    return minimo