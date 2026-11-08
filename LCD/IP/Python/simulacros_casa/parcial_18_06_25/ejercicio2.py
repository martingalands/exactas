#(cliente,m_pago,cant _prod)
from queue import Queue as Cola

# cola_prueba: Cola = Cola()
# cola_prueba.put(("Carlos","tarjeta",10))
# cola_prueba.put(("Lucas","tarjeta",1))
# cola_prueba.put(("Marta","efectivo",30))



def pasar_por_autoservicio(clientes:Cola[str,str,int])->str:    
    
    while not clientes.empty():
        cliente_actual: tuple[str,str,int] = clientes.get()
        cliente: str = cliente_actual[0]
        m_pago: str = cliente_actual[1]
        cant_prod: int = cliente_actual[2]
        if m_pago != 'efectivo' and cant_prod <= 15:
            res: str = cliente
            return res
        else:
            clientes.put(cliente_actual)


#print(pasar_por_autoservicio(cola_prueba))
#print(cola_prueba.queue)