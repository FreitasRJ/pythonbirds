import unittest
from mat import soma
from unittest import TestCase


class MatTestCase(TestCase):
    def teste_case(self):
             
        self.assertEqual(9,soma(4,5))

if __name__=='__main__':
    unittest.main()