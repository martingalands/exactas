def nivel_de_ocupacion(camas_por_piso:list[list[bool]])->list[float]:
    cantidad_camas_por_piso = len(camas_por_piso)
    res: list[float] = []
    for fila in range(len(camas_por_piso)):
        contador_piso:bool = 0
        for columna in range(len(camas_por_piso[fila])):
            cama: bool = camas_por_piso[fila][columna]
            if cama:
                contador_piso += 1
        res.append(cantidad_camas_por_piso/contador_piso)

    return res


mat = [[True,False,True],[False,True,True],[True,True,True]]

print(nivel_de_ocupacion(mat))