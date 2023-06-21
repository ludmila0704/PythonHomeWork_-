# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

FOUR_HUNDRED = 400  # год, номер которого кратен 400, — високосный
HUNDRED = 100  # остальные года, номер которых кратен 100, — невисокосные;
FOUR = 4  # остальные года, номер которых кратен 4, — високосные;


def input_print_year():
    year = int(input('Введите год, который хотите проверить на високосность:   '))
    print(f'{year} год {is_vis_year(year)}')


def is_vis_year(year):
    if (year % FOUR == 0 and year % HUNDRED != 0) or year % FOUR_HUNDRED == 0:
        return "високосный"
    else:
        return "не високосный"


input_print_year()
