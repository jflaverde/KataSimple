from unittest import TestCase

from SecuenciaNumeros import SecuenciaNumeros

class TestSecuenciaNumeros(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos(""), [0,0,0,0], "Cadena vacia")


class TestSecuenciaNumerosConUnNumero(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos("1"), [1,0,0,0], "Secuencia con un numero")

class TestSecuenciaNumerosConMultiplesNumeros(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos("1,2,3,4"), [4, 0, 0, 0], "Secuencia con multiples numeros")

