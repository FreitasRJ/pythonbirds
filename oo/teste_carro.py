# para teste no terminal digitar: python3 -m unittest discover

import unittest
from unittest import TestCase
from carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    
    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        self.assertEqual(2,motor.velocidade)

if __name__=='__main__':
    unittest.main()                                                                                                                                                                                                                                                                      
