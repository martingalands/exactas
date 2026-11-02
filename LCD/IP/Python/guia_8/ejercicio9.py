from queue import Queue as Cola

# cola_prueba:Cola = Cola()
# cola_prueba.put(10)
# cola_prueba.put(10)
# cola_prueba.put(10)
# cola_prueba.put(10)
# cola_prueba.put(10)

def cantidad_elementos(c:Cola)->int:
    contador: int = 0
    while not c.empty():
        c.get()
        contador += 1
    return contador

#print(cantidad_elementos(cola_prueba))


#print(cantidad_elementos(cola_prueba).get())

