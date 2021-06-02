import unittest
from polAlg import calcPol


class TestPolMethods(unittest.TestCase):

    def test_int(self)  :
        self.assertEqual(calcPol('4'), 4.0)

    def test_negative_int(self):
        self.assertEqual(calcPol('-4'), -4.0)

    def test_plus(self):
        self.assertEqual(calcPol('5+8'), 13.0)

    def test_minus(self):
        self.assertEqual(calcPol('8-5'), 3.0)

    def test_multiply(self):
        self.assertEqual(calcPol('8*5'), 40.0)

    def test_divide(self):
        self.assertEqual(calcPol('8/2'), 4.0)

    def test_divide_float_result(self):
        self.assertEqual(calcPol('15/2'), 7.5)

    def test_minus_negative_result(self):
        self.assertEqual(calcPol('15-17'), -2.0)

    def test_brackets(self):
        self.assertEqual(calcPol('4*(4-3)'), 4.0)

    def test_queue(self):
        self.assertEqual(calcPol('2+2*2'), 6.0)

    def test_queue_medium(self):
        self.assertEqual(calcPol('2+4*9/2'), 20.0)

    def test_queue_long(self):
        self.assertEqual(calcPol('-1*(2+4*9/2+9*(8-6))'), -38.0)

    def test_float_multiply(self):
        self.assertEqual(calcPol('1.4*2'), 2.8)

    def test_one_variable(self):
        self.assertEqual(calcPol('a', data={"a": 2}), 2.0)

    def test_two_variables_1(self):
        self.assertEqual(calcPol('a+b', data={"a": 2, "b": 3}), 5.0)

    def test_two_variables_2(self):
        self.assertEqual(calcPol('a+b', data={"a": -2, "b": 3}), 1.0)