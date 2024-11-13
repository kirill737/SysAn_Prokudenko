import numpy as np
from math import log2

# Универсальная функция для расчёта энтропии матрицы/массива
def calc_enthropy(matrix: list[list[int]]) -> float:
    H = 0
    for el in np.nditer(matrix):
        if el == 0:
            continue
        H -= el * log2(el)
    return H

# Функция для расчёта всех значений лабораторной
def calc_lab(matrix: list) -> float:
    matrix = np.array(matrix)
    total_count = np.sum(matrix) 
    # print(f"Суммарное кол-во эллементов в матрице: {total_count}")

    enthropy_matrix = matrix / total_count
    # enthropy_matrix = np.round(enthropy_matrix, 3)
    # print(enthropy_matrix)

    # Расчёт первым методом
    H_xy = calc_enthropy(enthropy_matrix)
    # print(f"H(XY): {round(H_xy, 2)}")

    p_y_array = np.sum(enthropy_matrix, axis=1)
    # print(f"p(y) array: {p_y_array}")
    p_x_array = np.sum(enthropy_matrix, axis=0)
    # print(f"p(x) array: {p_x_array}")

    H_y = calc_enthropy(p_y_array)
    # print(f"H(Y): {round(H_y, 2)}")

    H_x = calc_enthropy(p_x_array)
    # print(f"H(X): {round(H_x, 2)}")

    # Расчёт вторым методом
    rows_sum = np.sum(matrix, axis=1)
    # print(f"Rows sum: {rows_sum}")

    H_x_if_y = 0
    prefer_matrix = matrix.copy().astype(float)
    for r in range(len(matrix)):
        prefer_matrix[r] = prefer_matrix[r] / rows_sum[r]
        H_x_if_y += p_y_array[r] * calc_enthropy(prefer_matrix[r])
    I_x_if_y = H_x - H_x_if_y
    # print(prefer_matrix)
    # print(f"H(X|Y) / Ha(B): {round(H_x_if_y, 2)}")
    # print(f"I(X|Y): {round(I_x_if_y, 2)}")
    return np.array([round(H_xy, 2), round(H_x, 2), round(H_y, 2), round(H_x_if_y, 2), round(I_x_if_y, 2)]).tolist()

# Функция для создание матрицы из примера с кубиками
def create_cubes_example() -> list[list[int]]:
    subs =  {1, 2}
    for i in range(1, 7):
        for j in range(1, 7):
            subs.add(i * j)
    subs_ind = {}
    sums_ind = {}
    i = 0
    for el in sorted(subs):
        subs_ind[el] = i
        i += 1
    for i in range(2, 12 + 1):
        sums_ind[i] = i - 2
    cubes_matrix = np.zeros((11, 18))
    for i in range(1, 7):
        for j in range(1, 7):
            cubes_matrix[sums_ind[i + j], subs_ind[i * j]] += 1
    return cubes_matrix
# create_cubes_example()
def main() -> list[float]: 
    # Исходные данные с товарами
    pdf_example = [
        [20, 15, 10, 5],
        [30, 20, 15, 10],
        [25, 25, 20, 15],
        [20, 20, 25, 20],
        [15, 15, 30, 25]
    ]
    # Исходне данные для кубиков
    cubes_example = create_cubes_example()
    # calc_lab(create_cubes_example())
    # calc_lab(pdf_example)
    return calc_lab(cubes_example)
    # return calc_lab(pdf_example)
# print(main())
            
