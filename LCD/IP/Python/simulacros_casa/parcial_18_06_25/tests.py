import unittest

from ejercicio1 import *
from ejercicio2 import *

class Test(unittest.TestCase):
    def test_ejercicio_uno(self):
        self.assertEqual(cantidad_parejas_que_suman([3,2],5),1)
        self.assertEqual(cantidad_parejas_que_suman([3,2,2,1,4],5),2)
        self.assertEqual(cantidad_parejas_que_suman([1,1],2),1)
        self.assertEqual(cantidad_parejas_que_suman([0,0],0),1)
        self.assertNotEqual(cantidad_parejas_que_suman([1,1],2),0)

    def test_ejercicio_dos(self):
        cola_prueba: Cola = Cola()
        cola_prueba.put(("Ana", "efectivo", 13))
        cola_prueba.put(("Juan", "qr", 22))
        cola_prueba.put(("Bruno", "tarjeta", 14))
        

        self.assertNotEqual(pasar_por_autoservicio(cola_prueba), "Ana")
        #testeo que se mantengan las posiciones de cola luego de quitar a Bruno
        self.assertEqual(cola_prueba.queue[0][0], "Ana")
        self.assertEqual(cola_prueba.queue[1][0], "Juan")

        cola_prueba.put(("Carlos","tarjeta",10))
        cola_prueba.put(("Lucas","tarjeta",1))
        cola_prueba.put(("Marta","efectivo",30))

        self.assertEqual(pasar_por_autoservicio(cola_prueba), "Carlos")
        #testeo que se mantengan las posiciones de cola luego de quitar a Carlos
        self.assertEqual(cola_prueba.queue[0][0], "Lucas")
        self.assertEqual(cola_prueba.queue[1][0], "Marta")
        
        
        cola_prueba.put(("Carlos","efectivo",10))
        cola_prueba.put(("Lucas","efectivo",1))
        cola_prueba.put(("Marta","efectivo",30))

        self.assertNotEqual(pasar_por_autoservicio(cola_prueba), "Carlos")

        

    #def test_ejercicio_tres(self):