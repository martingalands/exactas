# import clase_pilas

import unittest


# class Test(unittest.TestCase):
#     def test_generar_pila_vacia(self):
#         pila = clase_pilas.generar_nros_al_azar(0,1,6)
#         self.assertTrue(pila.empty())

#     def test_generar_pila_con_10_elementos(self):
#         hasta = 6
#         desde = 1
#         pila = clase_pilas.generar_nros_al_azar(10,desde,hasta)
#         for i in range(hasta):
#             self.assertFalse(pila.empty())   # se asegura de que exista al menos un elemento para el get
#             x = pila.get()
#             self.assertTrue(desde <= x <= hasta)
#         self.assertTrue(pila.empty())


from queue import LifoQueue as Pila
from guia_8.ejercicio16 import *

class TestEjercicio16(unittest.TestCase):

    def generar_pila_vacia(self):
        pila = Pila()
        return pila


    def generar_dict_vacio(self,clave:str):
        diccionario: dict[str,Pila] = {}
        diccionario[clave] = self.generar_pila_vacia()
        return diccionario
    
    def test_nuevo_diccionario(self):
        historiales_test = self.generar_dict_vacio("martin")
        #self.assertTrue(historiales_test["martin"].get(),visitar_sitio(historiales,"martin"))
        self.assertFalse("camila" in visitar_sitio(historiales_test,"martin","www.google.cpm.ar").keys())



if __name__ == 'main':
    unittest.main(exit=False)