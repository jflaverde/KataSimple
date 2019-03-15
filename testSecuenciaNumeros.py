from unittest import TestCase

from SecuenciaNumeros import SecuenciaNumeros

class TestSecuenciaNumeros(TestCase):
    def test_procesarElementos(self):
        self.assertEqual(SecuenciaNumeros().procesarElementos(""), [0,0,0,0], "Cadena vacia")

