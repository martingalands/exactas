def agregar_producto(inventario:dict[str,dict[str,int | float]],nombre:str,precio:float,cantidad:int):
    if nombre not in inventario.keys():
        inventario[nombre] = {"precio":precio,"cantidad":cantidad}


inventario = {"silla":{"precio":2.62,"cantidad":5}}

# print(inventario)
# print(id(inventario))

agregar_producto(inventario,"cajonera",56.3,2)

# print(inventario)
# print(id(inventario))


def actualizar_stock(inventario:dict[str,dict[str,int | float]],nombre:str,cantidad:int):
    inventario[nombre]["cantidad"] = cantidad

# print(id(inventario))

#print(actualizar_stock(inventario,"cajonera",30))

# print(id(inventario))


def actualizar_precio(inventario:dict[str,dict[str,int | float]],nombre:str,precio:float):
    inventario[nombre]["precio"] = precio
    

#print(actualizar_stock(inventario,"cajonera",6.3))

def calcular_valor_inventario(inventario:dict[str,dict[str,int | float]])->float:
    suma : float = 0
    for art in inventario:
        suma += inventario[art]["cantidad"] * inventario[art]["precio"]
    return suma


#print(calcular_valor_inventario(inventario))

inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantal´on", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Deber´ıa imprimir 1100.0