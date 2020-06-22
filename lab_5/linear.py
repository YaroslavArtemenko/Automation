from math import exp, log, sin, cos, tan
from copy import deepcopy


def main(A, B, C):

    matrix = []

    for i in range(len(A) + 1):
        matrix.append([])
        leg = len(A[0])

        for j in range(leg + 2):
            if i == 0 and (j == 0 or j == 1):
                matrix[i].append('')
            elif i == 0:
                matrix[i].append(j-1)
            else:
                if j == 0:
                    matrix[i].append(i+len(C))
                elif j == 1:
                    matrix[i].append(B[i-1])
                else:
                    matrix[i].append(A[i-1][j-2])

    matrix.append([])
    ddd = len(A) + 2

    for j in range(len(C) + 2):
        if j == 0:
            matrix[ddd-1].append("Z")
        elif j == 1:
            matrix[ddd-1].append(0)
        else:
            matrix[ddd-1].append(C[j - 2])

    dop = True
    flag = True

    while(dop or flag):
        dop = True
        flag = False
        for i in range(1, len(matrix)-1):
            if matrix[i][1] < 0:
                flag = True
                break

        if flag == True:
            min_val = matrix[1][1]
            min_val_index = 1
            for i in range(1, len(matrix) - 1):
                try:
                    if matrix[i][1] < min_val:
                        min_val_index = i
                        min_val = matrix[i][1]
                except:
                    continue

            min_elem = matrix[min_val_index][2]
            min_elem_index = 2
            for i in range(2, len(matrix[0])):
                try:
                    if matrix[min_val_index][i] < min_elem:
                        min_elem_index = i
                except:
                    continue

        else:
            min_elem = matrix[-1][2]
            min_elem_index = 2
            for i in range(2, len(matrix[-1])):
                if matrix[-1][i] < min_elem:
                    min_elem_index = i
                    min_elem = matrix[-1][i]

            min_val = matrix[1][1] / matrix[1][min_elem_index]
            min_val_index = 1
            for i in range(1, len(matrix)-1):
                try:
                    if matrix[i][1] / matrix[i][min_elem_index] < min_val:
                        min_val_index = i
                except:
                    continue

        matrix[0][min_elem_index], matrix[min_val_index][0] = matrix[min_val_index][0], matrix[0][min_elem_index]
        old_matrix = deepcopy(matrix)
        matrix[min_val_index][min_elem_index] = 1 / matrix[min_val_index][min_elem_index]

        for i in range(1, len(matrix)):
            if i != min_val_index:
                matrix[i][min_elem_index] = -matrix[i][min_elem_index] * matrix[min_val_index][min_elem_index]

        for i in range(1, len(matrix[min_elem_index])):
            if i != min_elem_index:
                matrix[min_val_index][i] = matrix[min_val_index][i] * matrix[min_val_index][min_elem_index]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if i != min_val_index and j != min_elem_index:
                    matrix[i][j] = matrix[i][j] - old_matrix[min_val_index][j]*old_matrix[i][min_elem_index]*matrix[min_val_index][min_elem_index]

        dop = False
        for i in range(2, len(matrix[-1])):
            if matrix[-1][i] < 0:
                dop = True
                break

        flag = False
        for i in range(1, len(matrix) - 1):
            if matrix[i][1] < 0:
                flag = True
                break

    print("Результат: F(x) = ", matrix[-1][1], "\tx" + str(matrix[0][2]) + " = ", matrix[-1][2], "\tx" + str(matrix[0][3]) + " = ", matrix[-1][3])

