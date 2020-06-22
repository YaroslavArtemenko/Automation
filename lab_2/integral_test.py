import unittest
from integral import main
import random
import math

a='a'
b=2

a1 = 1
a2 = 2

a2 = 1
b2 = 9

aa = [random.randint(1, 10) for i in range(3)]
bb = [random.randint(1, 10) for i in range(3)]
print(aa)
print(bb)

def f(x):
    return (math.exp(1/x))/math.pow(x, 2)

def f1(x):
    return 1/x

class main_test(unittest.TestCase):
    def test_main(self):
        try: x = main(f, a, b)
        except TypeError:
            print("\n\n[{},{}] : НЕ ПОДХОДЯЩИЕ ДАННЫЕ".format(a, b))

        try:
            print("\n[{},{}] : ИНТЕГРАЛ С УСЛОВИЯ".format(1, 2))
            x = main(f ,1, 2)
        except:
            pass

        try:
            print("\n[{},{}] : ИНТЕГРАЛ ДЛЯ ПРИМЕРА".format(a2, b2))
            x = main(f1 ,a2, b2)
        except:
            pass

        for i in aa:
            for j in bb:
                try:
                    print("\n[{},{}] : Границы интеграла".format(i, j))
                    x = main(f, i, j)
                except: pass


if __name__=="__main__":
    unittest.main()
