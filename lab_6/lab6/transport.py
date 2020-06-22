from pulp import *

def main(a, b, C):

    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)
    x3 = pulp.LpVariable("x3", lowBound=0)
    x4 = pulp.LpVariable("x4", lowBound=0)
    x5 = pulp.LpVariable("x5", lowBound=0)
    x6 = pulp.LpVariable("x6", lowBound=0)
    x7 = pulp.LpVariable("x7", lowBound=0)
    x8 = pulp.LpVariable("x8", lowBound=0)
    x9 = pulp.LpVariable("x9", lowBound=0)
    x10 = pulp.LpVariable("x10", lowBound=0)
    x11 = pulp.LpVariable("x11", lowBound=0)
    x12 = pulp.LpVariable("x12", lowBound=0)
    x13 = pulp.LpVariable("x13", lowBound=0)
    x14 = pulp.LpVariable("x14", lowBound=0)
    x15 = pulp.LpVariable("x15", lowBound=0)
    x16 = pulp.LpVariable("x16", lowBound=0)
    x17 = pulp.LpVariable("x17", lowBound=0)
    x18 = pulp.LpVariable("x18", lowBound=0)
    x19 = pulp.LpVariable("x19", lowBound=0)
    x20 = pulp.LpVariable("x20", lowBound=0)
    problem = pulp.LpProblem('0', pulp.LpMaximize)
    problem += -C[0][0] * x1 - C[0][1] * x2 - C[0][2] * x3 - C[0][3] * x4 - C[0][4] * x5 \
               -C[1][0] * x6 - C[1][1] * x7 - C[1][2] * x8 - C[1][3] * x9 - C[1][4] * x10 \
               -C[2][0] * x11 - C[2][1] * x12 - C[2][2] * x13 - C[2][3] * x14 - C[2][4] * x15 \
               -C[3][0] * x16 - C[3][1] * x17 - C[3][2] * x18 - C[3][3] * x19 - C[3][4] * x20 , "Функция цели"
    problem += x1 + x2 + x3 + x4 + x5<= a[0], "1"
    problem += x6 + x7 + x8 + x9 + x10<= a[1], "2"
    problem += x11 + x12 + x13 + x14 + x15 <= a[2], "3"
    problem += x16 + x17 + x18 + x19 + x20 <= a[3], "4"
    problem += x1 + x6 + x11 + x16 == b[0], "5"
    problem += x2 + x7 + x12 + x17 == b[1], "6"
    problem += x3 + x8 + x13 + x18 == b[2], "7"
    problem += x4 + x9 + x14 + x19 == b[3], "8"
    problem += x5 + x10 + x15 + x20 == b[4], "9"
    problem.solve()
    result = {}
    result_unsort = {}
    for variable in problem.variables():
        result_unsort[variable.name] = variable.varValue
    for i in sorted(result_unsort.keys(), key= lambda x: int(x[1:])):
        result[i] = result_unsort[i]

    for i in result.keys():
        print(result[i], end=" ")

    cost = abs(value(problem.objective))
    print("Стоимость: ", cost)
    return result, cost
