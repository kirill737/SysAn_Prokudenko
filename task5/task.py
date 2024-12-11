import numpy as np

def calc_ranks(ranking):
    """
        Получает ранжировки
    """
    rankings = {}
    for level, group in enumerate(ranking):
        if isinstance(group, list):
            for item in group:
                rankings[item] = level
        else:
            rankings[group] = level
    return rankings

def calc_matrix(ranking):
    """
        Вычисляет матрицу согласований
    """
    rankings = calc_ranks(ranking)
    n = len(rankings)
    matrix = []

    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if rankings[j] >= rankings[i]:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    return matrix

def find_core_conflicts(matrix_a, matrix_b):
    """
        Вычисляет ядро противоречий
    """
    # print(np.array(matrix_a))
    # print(np.array(matrix_b))
    matrix_a, matrix_b = np.array(matrix_a), np.array(matrix_b)
    product_direct = matrix_a * matrix_b
    product_transposed = matrix_a.T * matrix_b.T
    conflict_matrix = np.logical_or(product_direct, product_transposed)
    
    conflicts = []
    for i in range(len(conflict_matrix)):
        for j in range(i + 1, len(conflict_matrix)):
            if not conflict_matrix[i, j] and not conflict_matrix[j, i]:
                conflicts.append([i + 1, j + 1])
    return conflicts

def main(ranking_a, ranking_b):
    # Вычисление матриц согласования
    matrix_a = calc_matrix(ranking_a)
    matrix_b = calc_matrix(ranking_b)

    # Получения ядра противоречий
    result = find_core_conflicts(matrix_a, matrix_b)

    return result

if __name__ == "__main__":
    # Тест из pdf
    A = [1, [2, 3], 4, 5]
    B = [[1, 2], 3, 5, 4]
    print(main(A, B))
    
    # Тест с Google диска
    A = [1, [2, 3], 4, [5, 6, 7], 8, 9, 10]
    B = [[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]
    print(main(A, B))