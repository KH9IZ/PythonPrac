import unittest
from unittest.mock import MagicMock
from prog import solve, SquareIO

class SolveSquareTestCase(unittest.TestCase):
    coeffs = {'a': '0', 'b': '0', 'c': '0'}
    def setUp(self):
        def inputCoeff(c):
            return self.coeffs[c]
        def printResult(x):
            self.x = x
        SquareIO.inputCoeff = MagicMock(side_effect=inputCoeff)
        SquareIO.printResult = MagicMock(side_effect=printResult) 
    
    def test_linear(self):
        self.coeffs = {'a': '0', 'b': '1', 'c': '1'}
        solve()
        self.assertEqual(self.x, -1)
    
    def test_square(self):
        self.coeffs = {'a': '1', 'b': '0', 'c': '-64'}
        solve()
        self.assertEqual(self.x, (-8, 8))

    def test_bad(self):
        self.coeffs = {'a': '0', 'b': '0', 'c': '1'}
        solve()
        self.assertIsNone(self.x)
        self.coeffs = {'a': 'lol', 'b': 'kek', 'c': 'cheburek'}
        with self.assertRaises(ValueError):
            solve()

if __name__ == "__main__":
    unittest.main()
