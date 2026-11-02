from queue import Queue as Cola

c1_prueba: Cola = Cola()
c2_prueba: Cola = Cola()

c1_prueba.put(1)
c1_prueba.put(3)
c2_prueba.put(2)
c2_prueba.put(4)

def intercalar(c1:Cola,c2:Cola)->Cola:
    c_res: Cola = Cola()
    while not c1.empty() and not c2.empty():
        c1_actual: int = c1.get()
        c2_actual: int = c2.get()
        c_res.put(c1_actual)
        c_res.put(c2_actual)
    #ultimo = c2.get()
    #c_res.put(ultimo)
    return c_res

#print(intercalar(c1_prueba,c2_prueba).queue)

