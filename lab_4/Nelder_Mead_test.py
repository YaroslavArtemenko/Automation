from Nelder_Mead import out
import unittest
from math import exp, sqrt

e = 0.00001


class TestCalc(unittest.TestCase):
    def test_0(self):
        print('Function 1: x**3 + y**3 - 3*x*y\n')
        res = out("x**3 + y**3 - 3*x*y", [0, 0], [0, 1], [1, 0], 34)
        self.assertTrue(abs(res[0][0] - 1) < e and abs(res[0][1] - 1) < e and abs(res[1] + 1) < e)

    def test_1(self):
        print('\n\nFunction 2: 5*(x - 3)**2 + (y - 5)**2+7\n')
        res = out("5*(x - 3)**2 + (y - 5)**2+7", [2, 6], [4, 4], [4, 3], 19)
        self.assertTrue(abs(res[0][0] - 3) < e and abs(res[0][1] - 5) < e and abs(res[1]-7) < e)

    def test_2(self):
        print('\n\nFunction 3: x**2 + y**2 + x*y\n')
        res = out("x**2 + y**2 + x*y", [1, 1], [0, 1], [1, 0], 2)
        self.assertTrue(abs(res[0][0]) < e and abs(res[0][1]) < e and abs(res[1]) < e)

    def test_3(self):
        print('\n\nFunction 4: (x-5)**2 + (y+3)**2 - 7\n')
        res = out("(x-5)**2 + (y+3)**2 - 7", [4, -2], [5, -2], [5, -4], 42)
        self.assertTrue(abs(res[0][0] - 5) < e and abs(res[0][1] + 3) < e and abs(res[1] + 7) < e)

    def test_4(self):
        print('\n\nFunction 5: x**2 + 4*y**2 + 1\n')
        res = out("x**2 + 4*y**2 + 1", [1, 1], [0, 1], [1, 0], 2)
        self.assertTrue(abs(res[0][0]) < e and abs(res[0][1]) < e and abs(res[1]-1) < e)

if __name__ == "__main__":
    unittest.main()