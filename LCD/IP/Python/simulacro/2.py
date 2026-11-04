from queue import Queue as Pila

pila_examenes: Pila = Pila()

pila_examenes.put(("Juan",2))
pila_examenes.put(("Caro",1))
pila_examenes.put(("Beto",2))
pila_examenes.put(("Ana",1))

# Ejercicio 2
# TODO: Implementar

    # #devuelvo todo en orden original a la pila
    # for i in range(len(lista_pila)):
    #     examenes.put(lista_pila[i])
    
    # #agrego todo en res (inevitablemente en orden de la pila 'examenes')
    # for i in range(len(lista_res)):
    #     res.put(lista_res[i])
    # return res

#[("Ana",1),("Beto",2),("Caro",1),("Juan",2)]

resultado = ejercicio2(pila_examenes)
print(resultado.get())
print(resultado.get())
print(pila_examenes.get())
print(pila_examenes.get())




#  problema ejercicio2 (inout examenes: Pila⟨String x Z⟩) : Pila⟨String⟩ {
#   requiere: { Todos los elementos de examenes tienen en la segunda componente de la tupla un 1 o un 2 }
#   requiere: { Todas las primeras componentes de tupla de examenes son distintas entre sí }
#   modifica: { examenes }
#   asegura: { res contiene exactamente los nombres cuya segunda componente en examenes@pre tenía tema = 1, en el mismo orden que se encontraban en examenes@pre }
#   asegura: { examenes contiene exactamente las tuplas de examenes@pre cuya segunda componente son tema = 2 allí, en el mismo orden que se encontraban originalmente .}
# }