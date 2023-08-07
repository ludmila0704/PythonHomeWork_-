from random import choice, randint

LETTERS_VOVS = 'aeiouy'
LETTERS_COWS = 'qwrtpsfghklzxcvbnm'
NAME_LENGTH_MIN = 4
NAME_LENGTH_MAX = 7


def psevdo_gen(num_names: int, file_num: str) -> None:
    """
    >>> psevdo_gen('r', 'text_psevdo.txt')
    Traceback (most recent call last):
    ...
    TypeError: Количество слов должно быть целого типа!
    >>> psevdo_gen(-6, 'text_psevdo.txt')
    Traceback (most recent call last):
    ...
    ValueError: Количество должно быть положительным!или не равно 0
    """
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
        raise TypeError('Количество слов должно быть целого типа!')


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
