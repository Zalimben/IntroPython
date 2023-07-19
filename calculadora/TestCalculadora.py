import unittest

from calculadora.Calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    """
    Clase para probar la calculadora
    """
    def test_suma_numeros_enteros_positivos_retorna_numero_positivo(self):
        # Dado que...
        nro1 = 21
        nro2 = 7
        calc = Calculadora()
        # Cuando...
        resultado = calc.suma(nro1, nro2)
        # Se obtiene...
        self.assertEqual(resultado, 28)
        self.assertTrue(resultado > 0)


    def test_resta_numeros_enteros_positivos_retorna_numero_negativo(self):
        # Dado que...
        nro1 = 17
        nro2 = 6
        calculadora = Calculadora()
        # Cuando...
        resultado = calculadora.resta(nro2, nro1)
        # Se obtiene...
        self.assertEqual(resultado, -11)
        self.assertTrue(resultado < 0)

    def test_resta_numeros_enteros_positivos_retorna_numero_positivo(self):
        # Dado que...
        nro1 = 17
        nro2 = 6
        calculadora = Calculadora()
        # Cuando...
        resultado = calculadora.resta(nro1, nro2)
        # Se obtiene...
        self.assertEqual(resultado, 11)
        self.assertTrue(resultado > 0)


    def test_multiplicar_nros_positivos_retorna_positivo(self):
        calculadora = Calculadora()
        nro1 = 2
        nro2 = 6
        resultado = calculadora.multiplicar(nro1, nro2)
        self.assertTrue(resultado > 0)

    def test_multiplicar_nro_por_zero_retorna_zero(self):
        calculadora = Calculadora()
        nro1 = 2
        nro2 = 0
        resultado = calculadora.multiplicar(nro1, nro2)
        self.assertTrue(resultado == 0)


    def test_multiplicar_nros_signos_diferentes_retorna_negativo(self):
        calculadora = Calculadora()
        nro1 = 2
        nro2 = -6
        resultado = calculadora.multiplicar(nro1, nro2)
        self.assertTrue(resultado < 0)


    def test_multiplicar_nros_negativos_retorna_positivo(self):
        calculadora = Calculadora()
        nro1 = -2
        nro2 = -6
        resultado = calculadora.multiplicar(nro1, nro2)
        self.assertTrue(resultado > 0)