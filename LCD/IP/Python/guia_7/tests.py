import unittest

from ejercicio2 import *

class Test(unittest.TestCase):

    def test_sin_vocales(self):
        self.assertEqual(sin_vocales("menem"),"mnm")
        self.assertNotEqual(sin_vocales("menem"),"menem")

    def test_promedio(self):
        self.assertEqual(promedio([10,10,10]),10)

    
    def test_menor_4(self):
        self.assertFalse(menor_4([3,2,2,5]))
        self.assertFalse(menor_4([4,5,8,9,8]))
        self.assertTrue(menor_4([1,2,3]))
        self.assertTrue(menor_4([]))


    def test_res_materia(self):
        self.assertEqual(resultado_materia([1,2,3]),3)
        self.assertNotEqual(resultado_materia([1,2,3]),2)

        #promedio 4 tiene que ser categoria 2 pues pn= 4 y m4 == False
        self.assertEqual(resultado_materia([4,4,4]),2)

        #veo si un promedio de 6.5 cae en la categoria 2
        self.assertAlmostEqual(resultado_materia([7,6]),2)

        #en cualquier otro caso categoria 1
        self.assertEqual(resultado_materia([10,10]),1)

    