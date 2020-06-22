from linear import main
import unittest
from math import exp, sqrt
import random


a = [random.randint(-10, 10) for i in range(20)]
a.append("A")
A_rand = [[[random.choice(a) for i in range(3)] for j in range(3)] for k in range(2)]
B_rand = [[random.choice(a) for j in range(3)] for k in range(2)]
C_rand = [[random.choice(a) for q in range(3)] for k in range(2)]

# УМОВА
A = [[1, 5], [3, 2], [2, 4], [2, 2], [1, 0]]
B = [10, 12, 16, 10, 1]
C = [-2, -3]

# # ЛІТЕРА "А"
# A0 = [[4, 2, 1], [6, 0, 2], [0, 2, 4], ['A', 7 , 0]]
# B0 = [150000, 170000, 100000, 200000]
# C0 = [-100, -150, -200]

#ПРИКЛАДИ
A1 = [[2, 5], [8, 5], [5, 6]]
B1 = [20, 40, 30]
C1 = [-50, -40]

A2 = [[4, 2, 1], [6, 0, 2], [0, 2, 4], [8, 7 , 0]]
B2 = [150000, 170000, 100000, 200000]
C2 = [-100, -150, -200]

class main_test(unittest.TestCase):
    def test_main(self):
        # try: x = main(A0, B0, C0)
        # except TypeError:
        #     print("\n\n[{}, {}, {}] : НЕ ПОДХОДЯЩИЕ ДАННЫЕ".format(A0, B0, C0))

        try:
            print("\n[{},{}, {}] : УСЛОВИЕ".format(A, B, C))
            x = main(A, B, C)
        except:
            pass

        try:
            print("\n[{},{}, {}] : ПРИМЕР №1".format(A1, B1, C1))
            x = main(A1, B1, C1)
        except:
            pass

        try:
            print("\n[{},{}, {}] : ПРИМЕР №2".format(A2, B2, C2))
            x = main(A2, B2, C2)
        except:
            pass

        for i in A_rand:
            for j in B_rand:
                for q in C_rand:
                    try:
                        x = main(i, j, q)
                    except TypeError:
                        print("\n\n[{},{}, {}]: Не подходящие данные".format(i, j, q))



if __name__ == "__main__":
    unittest.main()
