import unittest
from prog import solveSquare

class SolveSquareTestCase(unittest.TestCase):
    def test_positive_discr(self):
        roots = solveSquare(1, 5, 4)
        self.assertTupleEqual(roots, (-4, -1))
        roots = solveSquare(-1, 5, -4)
        self.assertTupleEqual(roots, (1, 4))
        roots = solveSquare(2, 6, 3)
        self.assertAlmostEqual(roots[0], -2.37, places=2)
        self.assertAlmostEqual(roots[1], -0.63, places=2)
        roots = solveSquare(-2, 6, -3)
        self.assertAlmostEqual(roots[1], 2.37, places=2)
        self.assertAlmostEqual(roots[0], 0.63, places=2)

    def test_zero_discr(self):
        roots = solveSquare(1, 4, 4)
        self.assertTupleEqual(roots, (-2, -2))
        roots = solveSquare(-1, 4, -4)
        self.assertTupleEqual(roots, (2, 2))
        roots = solveSquare(2.3, 0.7, 0.053260869565)
        self.assertAlmostEqual(roots[0], roots[1], places=11)

    def test_negative_discr(self):
        roots = solveSquare(1, 1, 1)
        self.assertIsNone(roots)

if __name__ == "__main__":
    unittest.main()
