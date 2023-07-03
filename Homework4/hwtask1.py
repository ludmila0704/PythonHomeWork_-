import random

import numpy as np

ZERO = 0
MIN_NUM = 0
MAX_NUM = 100


def matr_transpon(matr: np.array([[int], [int], [int]])) -> np.array([[int], [int], [int]]):
    matr_res = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for i in range(len(matr)):
        for j in range(len(matr[ZERO])):  # столбец
            matr_res[j][i] = matr[i][j]
    return matr_res


def matr_random() -> np.array([[int], [int], [int]]):
    matr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for i in range(len(matr)):
        for j in range(len(matr[ZERO])):
            matr[i][j] = random.randint(MIN_NUM, MAX_NUM)
    return matr


arr = matr_random()
arr1 = matr_transpon(arr)

if __name__ == '__main__':
    print(f'Исходная матрица:  ')
    print(f'{arr}')
    print(f'Транспонированная матрица: ')
    print(f'{arr1}')
