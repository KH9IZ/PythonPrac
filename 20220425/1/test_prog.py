import unittest
from prog import solve

class SolverTestCase(unittest.TestCase):
    def test_solve(self):
        self.assertIsNone(solve(0, 0))
        self.assertIsNone(solve(0, 1))
        self.assertEqual(solve(1, 1), -1.0)
        self.assertAlmostEqual(solve(2424.3423421, 331.3439), -0.13667372558983776)

if __name__ == "__main__":
    unittest.main()
