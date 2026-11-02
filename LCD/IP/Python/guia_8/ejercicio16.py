from queue import LifoQueue as Pila
#nombre_usuario

pila_test: Pila = Pila()   #creo una instancia Pila de clase Pila
pila_test.queue.extend(["www.disneyplus.com.ar","www.twitter.com","www.infobae.com.ar"])  #esto sirve para testing. creo varias apilaciones

historiales: dict[str]
#historiales = {"martin":pila_test}


def visitar_sitio(historiales:dict[str,Pila],usuario:str,sitio:str):
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        nueva_pila: Pila = Pila()
        nueva_pila.put(sitio)   #el metodo devuelve None, guarda con las asignaciones
        historiales[usuario] = nueva_pila

#print(visitar_sitio(historiales, "camila","www.google.com.ar"))
#print(historiales["martin"].get())
#print(historiales["camila"].get())

