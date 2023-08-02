# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import choice, randint

LETTERS_VOVS = 'aeiouy'
LETTERS_COWS = 'qwrtpsfghklzxcvbnm'
NAME_LENGTH_MIN = 4
NAME_LENGTH_MAX = 7


def psevdo_gen(num_names: int, file_num: str) -> None:
    if isinstance(num_names, int):
        if num_names > 0:
            with open(file_num, 'a', encoding='utf-8') as f:
                for _ in range(num_names):
                    name = ''.join(choice(LETTERS_VOVS) if i in (1, 4, 6)
                                   else choice(LETTERS_COWS) for i in range(randint(NAME_LENGTH_MAX, NAME_LENGTH_MAX)))

                    f.write(f'{name.capitalize()}\n')
        else:
            raise ValueError('Количество должно быть положительным!или не равно 0')
    else:
        raise ValueError('Количество слов должно быть целого типа!')


if __name__ == "__main__":
    psevdo_gen('r', 'text_psevdo.txt')
    psevdo_gen(-6, 'text_psevdo.txt')
    psevdo_gen(6, 'text_psevdo.txt')
