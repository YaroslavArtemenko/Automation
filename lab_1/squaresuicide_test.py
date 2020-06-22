import unittest
from squaresuicide import SS
import random

minus = []
a = [random.randint(-10, 10) for i in range(20)]
a.append("A")
matrix = [[[random.choice(a) for i in range(4)] for j in range(4)] for k in range(9)]
matrix.append([[4.31, 0.26, 0.61, 0.27],  # adekvat
             [0.26, 2.32, 0.18, 0.34],
             [0.61, 0.18, 3.2, 0.31],
             [0.27, 0.34, 0.31, 5.17]])
matrix.append([[2, -5, 2, -2],
               [2, 3, -1, 2],
               [3, -3, 2, -2],
               [1, 1, -1, 2]])
matrix.append([[8.7, -2.2, -1.1, -0.7],
                  [-2.2, 10, 2.3, -0.7],
                  [-1.1, 2.3, -5.1, 2.8],
                  [-0.7, -0.7, 2.8, 7.9, 20]])
matrix.append([[1,1,1,1],
               [1,-1,-1,-1],
               [2,-1,1,0],
              [3,5,4,10]])

class SS_test(unittest.TestCase):

    def test_SS(self):
        for A in matrix:
            B = [6,-4,1,26]
            try:
                self.assertEqual(len(A), 4)
            except AssertionError:
                print("{}: Не 4 строчки".format(A))
                minus.append(A)
            for row in A:
                try:
                    self.assertEqual(len(row), 4)
                except AssertionError:
                    print("{}: Не 4 cтолбца".format(A))
                    minus.append(A)
                    break
            try: x = SS(A,B)
            except TypeError:
                minus.append(A)
                print("{}: Не подходящие данные".format(A))

            except ZeroDivisionError:
                minus.append(A)
                print("{}: Деление на 0".format(A))
        for A in minus:
            try:
                matrix.remove(A)
            except: pass
        for A in matrix:
            try:
                x = SS(A, B)
                print("\n\n{} \n{}".format(A,x))
            except: pass



if __name__=="__main__":
    unittest.main()