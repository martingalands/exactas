from queue import Queue as Cola

# cola_prueba: Cola = Cola()
# cola_prueba.put(10)
# cola_prueba.put(6)
# cola_prueba.put(55)

def buscar_el_maximo(c:Cola[int])->int:
    maximo : int = 0
    while not c.empty():
        valor_actual: int = cola_prueba.get()
        if valor_actual > maximo:
            maximo = valor_actual
    return maximo

#print(buscar_el_maximo(cola_prueba))