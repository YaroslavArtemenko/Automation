import math

print("Используем формулу левых прямоугольников")
print("Интегрируемая функция: f(x) = (e^(1/x))/x^2")
print("Точность: 0.001")

def work(f, a, b, n):
    #print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    #print("Текущий шаг:", h)
    total = sum([f((a + (k*h))) for k in range(0, n)])
    result = h * total
    #print("Текущий результат: ", result)
    return result


def main(f, a, b):
    n = 2
    a1 = work(f, a, b, n)
    n *= 2
    a2 = work(f, a, b, n)

    while abs(a1 - a2) > 0.00001:
        n *= 2
        a1 = work(f, a, b, n)
        n *= 2
        a2 = work(f, a, b, n)

    print("\nОтвет:", a2, "\nКоличество разбиений:", n)

#main(1, 2)