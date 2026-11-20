# Una fábrica recibe pedidos de distintos productos, cada uno con la cantidad de unidades que se necesitan, y los guarda en una cola en orden de llegada. La máquina trabaja por turnos: en cada turno toma el primer pedido de la cola y produce hasta capacidad unidades de ese producto (o todas las pendientes, si son menos que capacidad). Si al terminar el turno quedan unidades pendientes de ese producto, el pedido vuelve al final de la cola con las unidades que faltan. Implementar la función producir_por_turnos, que vacía la cola y devuelve, en orden, cuántas unidades de qué producto se produjeron en cada turno.

# problema producir_por_turnos (inout pedidos: Cola⟨String x Z⟩, in capacidad: Z) : seq⟨String x Z⟩ {
#   requiere: { capacidad > 0 }
#   requiere: { Las primeras componentes de pedidos son strings no vacíos y todos distintos entre sí }
#   requiere: { Las segundas componentes de pedidos son números mayores o iguales a 1 }
#   modifica: { pedidos }
#   asegura: { pedidos queda vacía }
#   asegura: { Para todo turno t de res, si las unidades pendientes del producto de t al comenzar ese turno son mayores o iguales a capacidad,
#   la segunda componente de t es igual a capacidad; si no, es igual a esas unidades pendientes }
#   asegura: { res contiene solamente productos que estuvieran en pedidos@pre }
#   asegura: { Para cada producto p de pedidos@pre, la suma de las segundas componentes de los turnos de res cuya primera componente es p es igual a las unidades que tenía asociadas p en pedidos@pre }
#   asegura: { El orden de los turnos en res es el orden en que se fueron realizando los turnos de producción }
# }

from queue import Queue as Cola

pedidos_test = Cola()

pedidos_test.put(("A",7))
pedidos_test.put(("B",5))
pedidos_test.put(("C",5))
pedidos_test.put(("D",6))

# pedidos_test.put(("A",1))
# pedidos_test.put(("B",1))
# pedidos_test.put(("C",1))



def producir_por_turnos(pedidos,capacidad:int)->list[str,int]:
    res: list[tuple[str,int]] = []
    pendientes: list[tuple[str,int]] = []
    while not pedidos.empty():
        pedido_actual:tuple[str,int] = pedidos.get()

        articulo:str = pedido_actual[0]
        cantidad:int = pedido_actual[1]

        if cantidad >= capacidad:
            res.append((articulo,capacidad))
            if cantidad-capacidad >0:
                pedidos.put((articulo,cantidad-capacidad))
        else:
            res.append((articulo,cantidad))

    return res


print(producir_por_turnos(pedidos_test,6))



