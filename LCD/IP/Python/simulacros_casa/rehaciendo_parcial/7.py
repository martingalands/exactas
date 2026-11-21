def productos_faltantes(inventario:dict[str,int],pedidos:list[dict[str,int]])->dict[str,int]:
    dict_total = pedido_total(pedidos)
    res:dict[str,int] = {}
    for clave in dict_total.keys():
        valor:int = dict_total[clave]
        if clave not in inventario.keys():
            res[clave] = valor
        else:
            cantidad_en_inventario:int = inventario[clave]
            if valor > cantidad_en_inventario:
                res[clave] = valor-cantidad_en_inventario

    return res


#funcion para agrupar pedidos en un diccionario unico
def pedido_total(p):
    #agarro el primer elemento de la lista
    dict_res:dict[str,int] = {}
    for pedido in p:
        for clave in pedido.keys():
            valor = pedido[clave]
            if clave in dict_res:
                dict_res[clave] += valor
            else:
                dict_res[clave] = valor

    return dict_res






print(productos_faltantes({"lapiz": 10, "goma": 2, "regla": 5},[{"lapiz": 6, "goma": 1}, {"lapiz": 4, "cuaderno": 3}, {"goma": 2, "regla": 4}]))