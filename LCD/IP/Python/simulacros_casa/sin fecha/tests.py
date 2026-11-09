import unittest

from ejercicio4 import *

class Test(unittest.TestCase):
    def test_ejercicio_cuatro(self):
        self.assertEqual(palabras_por_vocales("hola soy yo"),{2:1,1:2})
        self.assertEqual(palabras_por_vocales("hola dios   soy yo de nuevo  "),{2:2,1:3,3:1})
