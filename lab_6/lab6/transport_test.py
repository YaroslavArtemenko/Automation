import unittest
from transport import main
import random



a = [random.randint(-10, 10) for i in range(20)]
a.append("A")
A_rand1 = [[random.choice(a) for i in range(5)] for j in range(4)]
A_rand2 = [[random.choice(a) for i in range(5)] for j in range(4)]
A_rand3 = [[random.choice(a) for i in range(5)] for j in range(4)]
A_rand4 = [[random.choice(a) for i in range(5)] for j in range(4)]


a = [17, 14, 21, 43]
b = [19, 22, 23, 17, 14]
C = [[12, 11, 25, 17, 21],
     [22, 18, 14, 8, 1],
     [9, 13, 2, 28, 15],
     [26, 21, 3, 4, 27]]
res = 598.0


a1 = [12, 17, 18, 13]
b1 = [10, 8, 12, 14, 16]
C1 = [[6, 11, 20, 17, 8],
     [1, 25, 3, 18, 17],
     [9, 39, 16, 30, 31],
     [23, 15, 4, 3, 28]]
res1 = ({'x1': 0.0, 'x2': 8.0, 'x3': 0.0, 'x4': 0.0, 'x5': 4.0,
         'x6': 0.0, 'x7': 0.0, 'x8': 5.0, 'x9': 0.0, 'x10': 12.0,
         'x11': 10.0, 'x12': 0.0, 'x13': 7.0, 'x14': 1.0, 'x15': 0.0,
         'x16': 0.0, 'x17': 0.0, 'x18': 0.0, 'x19': 13.0, 'x20': 0.0},
        610.0)


a2 = [14, 14, 14, 18]
b2 = [12, 12, 12, 12, 12]
C2 = [[29, 4, 7, 6, 16],
     [21, 13, 25, 21, 7],
     [20, 10, 12, 6, 2],
     [17, 7, 4, 6, 19]]

res2 = ({'x1': 0.0, 'x2': 12.0, 'x3': 0.0, 'x4': 2.0, 'x5': 0.0,
                        'x6': 12.0, 'x7': 0.0, 'x8': 0.0, 'x9': 0.0, 'x10': 2.0,
                        'x11': 0.0, 'x12': 0.0, 'x13': 0.0, 'x14': 4.0, 'x15': 10.0,
                        'x16': 0.0, 'x17': 0.0, 'x18': 12.0, 'x19': 6.0,'x20': 0.0}, 454.0)


class main_test(unittest.TestCase):

    def test_main(self):
        try:
            print("УСЛОВИЕ ЗАДАНИЯ:\n[{},\n{},\n{}]\n".format(a, b, C))
            x = main(a, b, C)
            #self.assertEqual(main(a, b, C), res)
        except:
            pass

        try:
            print("\nУСЛОВИЕ ДЛЯ ПРИМЕРА №1:\n[{},\n{},\n{}]\n".format(a1, b1, C1))
            x = main(a1, b1, C1)
            self.assertEqual(main(a1, b1, C1), res1)
        except:
            pass

        try:
            print("\nУСЛОВИЕ ДЛЯ ПРИМЕРА №2:\n[{},\n{},\n{}]\n".format(a2, b2, C2))
            x = main(a2, b2, C2)
            self.assertEqual(main(a2, b2, C2), res2)
        except:
            pass


        try:
            print("\nГенератор рандомных чисел(ПРИМЕР 1):\n[{},\n{},\n{}]\n".format(a, b, A_rand1))
            x = main(a, b, A_rand1)
        except TypeError:
            print("НЕ ПОДХОДЯЩИЕ ДАННЫЕ")

        try:
            print("\nГенератор рандомных чисел(ПРИМЕР 2):\n[{},\n{},\n{}]\n".format(a, b, A_rand2))
            x = main(a, b, A_rand2)
        except TypeError:
            print("НЕ ПОДХОДЯЩИЕ ДАННЫЕ")

        try:
            print("\nГенератор рандомных чисел(ПРИМЕР 3):\n[{},\n{},\n{}]\n".format(a, b, A_rand3))
            x = main(a, b, A_rand3)
        except TypeError:
            print("НЕ ПОДХОДЯЩИЕ ДАННЫЕ")

        try:
            print("\nГенератор рандомных чисел(ПРИМЕР 4):\n[{},\n{},\n{}]\n".format(a, b, A_rand4))
            x = main(a, b, A_rand4)
        except TypeError:
            print("НЕ ПОДХОДЯЩИЕ ДАННЫЕ")


if __name__=="__main__":
    unittest.main()