# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


def guessing(text: str, variants: [str], counts: int) -> int:
    print(f'Ваша загадка на сегодня {text}')

    for count in range(1, counts + 1):
        answer = (input(f'Попытка {count} . Введите отгадку: '))
        if answer in variants:
            print('Вы угадали')
            return count

    print(f'Вы не угадали за {counts} попытки')
    return 0


def guesses_dict(g_dict: [str, [str]], count: int = 3) -> None:
    for key, value in g_dict.items():
        res = guessing(key, value, count)
        print(f'\nCode {res}')


if __name__ == "__main__":
    # guess='Зимой и летом одним цветом'
    # answer_vars=['Елка','елка','ель','сосна']
    # answer_counts=3
    #
    # res=guessing(guess,answer_vars,answer_counts)
    # print(res)
    guesses = {'Зимой и летом одним цветом': ['Елка', 'елка', 'ель', 'сосна'],
               'Висит груша , нельзя скушать': ['Лампа', 'лампочка']}
    guesses_dict(guesses)
