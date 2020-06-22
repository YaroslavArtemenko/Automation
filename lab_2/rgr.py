import math



print("Розрахунково графічна робота")
print("Артеменко Ярослав КМ-63")
print("Метод лівих прямокутників")
print("Функція, яка інтегрується: f(x) = (e^(1/x))/x^2")
# print("Функція, яка інтегрується: f(x) = 1/x")



# def f(x):
#     return (math.exp(1 / x)) / math.pow(x, 2)

# def f(x):
#     return 1/x

def f(x):
    return(x*x)

def work(f, a, b, n):
    # print("\nТекущее число разбиений: ", n)
    h = (b - a) / float(n)
    # print("Текущий шаг:", h)
    total = sum([f((a + (k * h))) for k in range(0, n)])
    result = h * total
    # print("Текущий результат: ", result)
    return result



def main(f, a, b, eps):
    n = 2
    a1 = work(f, 1, 2, n)
    n *= 2
    a2 = work(f, 1, 2, n)

    while abs(a1 - a2) > eps:
        n *= 2
        a1 = work(f, a, b, n)
        n *= 2
        a2 = work(f, a, b, n)

    print("\nВідповідь: ", a2, "\nКількість розбиттів:", n)
eps = float(input('\n\nВведіть точність: eps = '))
a = int(input('\nВведіть нижню межу: a = '))
b = int(input('\nВведіть верхню межу: b = '))
main(f, a, b, eps)

