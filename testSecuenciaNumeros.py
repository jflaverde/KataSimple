from unittest import TestCase

from SecuenciaNumeros import SecuenciaNumeros

class TestSecuenciaNumeros(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos(""), [0,0,0,0], "Cadena vacia")


class TestSecuenciaNumerosConUnNumero(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos("1"), [1,1,1,1], "Secuencia con un numero")
        self.assertEqual(SecuenciaNumeros().procesarElementos("2"), [1,2,2,2], "Secuencia con un numero")

class TestSecuenciaNumerosConMultiplesNumeros(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos("1,2,3,4"), [4, 1, 4, 2.5], "Secuencia con multiples numeros")
        self.assertEqual(SecuenciaNumeros().procesarElementos("4,3,2,1"), [4, 1, 4, 2.5], "Secuencia con multiples numeros")

class TestSecuenciaNumerosConMultiplesNumerosYAmpersand(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos("1&2&3&4"), [4, 1, 4, 2.5], "Secuencia con multiples numeros")

class TestSecuenciaNumerosConMultiplesNumerosYDosPuntos(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos("1:2:3:4"), [4, 1, 4, 2.5], "Secuencia con multiples numeros")
