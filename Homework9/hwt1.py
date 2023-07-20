
import math
import cmath
from random import randint
from typing import Callable
import csv
import json
import os


def get_root_random_a_b_c_fom_csv(file: str):
    def get_root(func: Callable):
        def wrapper(*args, **kwargs):
            with open(file, 'r', encoding='utf-8') as f1:
                csv_file = csv.DictReader(f1, dialect='excel-tab')
                for line in csv_file:
                    num1 = int(line.get("a"))
                    num2 = int(line.get("b"))
                    num3 = int(line.get("c"))
                    args = num1, num2, num3
                    result = func(*args, **kwargs)
                    yield args, result

        return wrapper

    return get_root


def logger(func: Callable):
    file_name = 'logger.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            args, result = result

            if result:
                json_dict = {'args': args, **kwargs,'result':result}
                json_dict['result'] = result
                data.append(json_dict)
                with open(file_name, 'w', encoding='utf-8') as f1:

                    json.dump(data, f1, ensure_ascii=False)
            else:
                break

    return wrapper


@logger
@get_root_random_a_b_c_fom_csv('csv_random.csv')
def get_root_quadratic_eq(num_a: int, num_b: int, num_c: int, *args, **kwargs):
    if num_a!=0:

        d = num_b ** 2 - 4 * num_a * num_c
        if d == 0:
            x1 = (-num_b) / 2 * num_a
            return x1
        elif d > 0:
            x1 = (-num_b + math.sqrt(d)) / 2 * num_a
            x2 = (-num_b - math.sqrt(d)) / 2 * num_a
            return round(x1,2), round(x2,2)
        else:

            return 'не существует'
    else:
        return 0,0


def gen_csv_file_with_random_numbers(count_rows: int = 100, MIN_NUM: int = -100, MAX_NUM=100):
    data_list = []
    for i in range(count_rows):
        data_list.append({'a': randint(1, MAX_NUM), 'b': randint(MIN_NUM, MAX_NUM), 'c': randint(-MIN_NUM, MAX_NUM)})

    with open('csv_random.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['a', 'b', 'c'], dialect='excel-tab')
        writer.writeheader()
        writer.writerows(data_list)


if __name__ == "__main__":
    gen_csv_file_with_random_numbers()
    res=(get_root_quadratic_eq())
