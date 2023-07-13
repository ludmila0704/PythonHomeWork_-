# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции
import random

MAX_NUM = 1000
MIN_NUM = -1000


def rand_pares(num_str: int, file_num: str) -> None:
    with open('text.txt', 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            f.write(f'{random.randint(MIN_NUM, MAX_NUM)} | {random.uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == "__main__":
    rand_pares(7, 'text.txt')
