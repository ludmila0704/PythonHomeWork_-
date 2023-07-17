# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os


def add_user(path: str) -> None:
    tmp_set = set()
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as j:
            my_dict = json.load(j)
        for _, val in my_dict.items():
            tmp_set.update(val.keys())
    else:
        my_dict = {i: {} for i in range(1, 8)}

    while True:
        name = input("Введите имя:  ")
        id_name = input("Введите личный идентификатор:  ")
        level = int(input("Введите уровень доступа(от 1 до 7):  "))

        if id_name in tmp_set and my_dict[level].get(id_name) is None:
            continue
        tmp_set.update(id_name)
        my_dict[level].update({id_name: name})
        with open(path, 'w', encoding='utf-8') as j:
            json.dump(my_dict, j, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    add_user('s8t2.json')
