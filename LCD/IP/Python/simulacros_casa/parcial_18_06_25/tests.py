import unittest

from ejercicio1 import *
from ejercicio2 import *
from ejercicio3 import *
from ejercicio4 import *

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


    def test_ejercicio_cuatro(self):
        self.assertEqual(mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'}),{'Merlo':1})
        self.assertNotEqual(mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Ituzaingo'}),{'Merlo':1})
        self.assertEqual(mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Merlo', 'Ana': 'Merlo'}),{'Merlo':2})
        

    def test_ejercicio_tres(self):
        mat = [[1,2,3],
       [40,50,60],
       [-7,-8,-9]]

        #verifico que la direccion en memoria sea la misma y testeo funcionamiento
        id_mat = id(mat)
        copia_mat = mat.copy()
        intercambiar_e_invertir_columnas(mat,1,2)
        self.assertNotEqual(copia_mat,[[1, -9, -8], [40, 60, 50], [-7, 3, 2]])
        id_mat_luego= id(mat)
        self.assertEqual(id_mat,id_mat_luego)