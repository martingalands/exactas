from queue import LifoQueue as Pila

p1:Pila=Pila()
p2:Pila=Pila()

p2.put(2)
p2.put(4)
p2.put(6)
p2.put(8)

p1.put(1)
p1.put(3)
p1.put(5)
p1.put(7)


def intercalar(p1:Pila,p2:Pila)->Pila:
    res_lista:list[int] = []
    while not p2.empty():
        elem2:int=p2.get()
        res_lista.append(elem2)
        elem1:int=p1.get()
        res_lista.append(elem1)
    res : Pila = Pila()
    for elem in res_lista:
        res.put(elem)
    return res


pila_demo = intercalar(p1,p2)
while not pila_demo.empty():
    print(pila_demo.get())

    
