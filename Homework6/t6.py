# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

_result= {}
def guessing(text: str, variants: list[str], counts: int) -> int:
    print(f'Ваша загадка на сегодня {text}')

    for count in range(1, counts + 1):
        answer = int(f'Попытка {count} . Введите отгадку: ')
        if answer in variants:
            print('Вы угадали')
            return count

    print(f'Вы не угадали за {counts}')
    return 0


def guesses_dict(g_dict: dict[str, list[str]], count: int = 3) -> None:
    for key, value in g_dict.items():
        res = guessing(key, value, count)
        result_score(key,res)
        print(f'\nCode {res}')

def result_score(txt:str,count_num: int)->None:
    _result.update({txt:count_num})

def printing_statistic():
    res=(f'Загадка {key} отгадана за {value} попыток.' if value >0 \
        else f'агадка {key} не отгадана за все попытки'
        for key,value in _result.items())
    print("\n".join(res))

if __name__ == "__main__":
    # guess='Зимой и летом одним цветом'
    # answer_vars=['Елка','елка','ель','сосна']
    # answer_counts=3
    #
    # res=guessing(guess,answer_vars,answer_counts)
    # print(res)
    guesses = {'Зимой и летом одним цветом': ['Елка', 'елка', 'ель', 'сосна']}
    guesses_dict(guesses)
