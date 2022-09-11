from unittest import TestCase
from carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        motor.velocidade
        self.assertEqual(0, motor.velocidade)
