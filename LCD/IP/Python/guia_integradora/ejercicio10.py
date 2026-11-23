# Ejercicio 10. Cola en el Banco
# En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por
# las tuplas (nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser ”com´un” o ”vip”.
# Se nos pide implementar una funci´on en python que dada una cola de clientes del banco, devuelva una nueva cola con los
# mismos clientes pero en donde los clientes vip est´an primero que los clientes comunes manteniendo el orden original de los clientes
# vips y los comunes entre s´ı.

# problema reordenar cola priorizando vips (in filaClientes: Cola<str × str>) : Cola<str> {
# requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0.}
# requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son ”com´un” o ”vip”.}
# requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre s´ı.}
# asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes.}
# asegura: {|res| = |filaCliente|.}
# asegura: {res no tiene elementos repetidos.}
# asegura: {No hay ning´un cliente ”com´un” antes que un ”vip” en res.}
# asegura: {Para todo cliente c1 y cliente c2 de tipo ”com´un” pertenecientes a filaClientes si c1 aparece antes que c2 en
# filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
# asegura: {Para todo cliente c1 y cliente c2 de tipo ”vip” pertenecientes a filaClientes si c1 aparece antes que c2 en
# filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
# }


from queue import Queue as Cola

prueba = Cola()

prueba.put(("juan","comun"))
# prueba.put(("carlos","comun"))
prueba.put(("lucia","vip"))
# prueba.put(("carla","comun"))
# prueba.put(("esteban","comun"))
# prueba.put(("pedro","vip"))


def reordenar_cola_priorizando_vips(filaClientes: Cola[str,str])->Cola[str]:
    vips:list[tuple[str,str]] = []
    comunes:list[tuple[str,str]] = []
    while not filaClientes.empty():
        cliente:tuple[str,str] = filaClientes.get()
        tipo_cliente:str = cliente[1]
        if tipo_cliente == "vip":
            vips.append(cliente)
        else:
            comunes.append(cliente)
    
    colares:Cola = Cola()

    for vip in vips:
        colares.put(vip)
    for comun in comunes:
        colares.put(comun)

    return colares


print(reordenar_cola_priorizando_vips(prueba).queue)

    