import clase_pilas

import unittest


class Test(unittest.TestCase):
    def test_generar_pila_vacia(self):
        pila = clase_pilas.generar_nros_al_azar(0,1,6)
        self.assertTrue(pila.empty())

    def test_generar_pila_con_10_elementos(self):
        hasta = 6
        desde = 1
        pila = clase_pilas.generar_nros_al_azar(10,desde,hasta)
        for i in range(hasta):
            self.assertFalse(pila.empty())   # se asegura de que exista al menos un elemento para el get
            x = pila.get()
            self.assertTrue(desde <= x <= hasta)
        self.assertTrue(pila.empty())


if __name__ == 'main':
    unittest.main(exit=False)