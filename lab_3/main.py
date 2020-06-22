from math import exp, log, sin, cos, tan

class Diapason(Exception):
    def __init__(self, text):
        self.text = text


def inputs(f, a, b, x, y, h):
    try:
        if a > b:
            raise Diapason("a > b")
        x_l = [x]
        y_l = [y]
        i = 0
        while x_l[i] < b:
            y_l.append(y_l[i] + trapezoidal(f, x_l[i], y_l[i], h))
            x_l.append(round(x_l[i] + h, 5))
            i+=1
        res = x_l ,y_l
    except NameError:
        res = "Неправильна вхідна функція"
    except Diapason as e:
        return str(e)

    return res


def trapezoidal(f, x, y, h):
    k = []
    k.append(func(x, y, f))
    k.append(func(x + h/2, y + h*k[0]/2, f))
    k.append(func(x + h / 2, y + h * k[1] / 2, f))
    k.append(func(x + h, y + h * k[2], f))

    result = h/6 * (k[0] + 2*k[1] + 2*k[2] + k[3])
    return result


def func(x, y, func):
    dd = eval(func)
    return dd



res = inputs("-(x+y)/x", 1, 3, 1, 1/2, 0.1)

print(res)