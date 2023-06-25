# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.
SS = 16  # система счисления
TEN = 10
ELEVEN = 11
TWELVE = 12
THIRTEEN = 13
FOURTEEN = 14
FIFTEEN = 15


def trans_in_16():
    number = int(input('Введите число,которое хотите перевести в 16-ричное представление:   '))
    print(f'{number} это {fun_trans_in_16(number)}. Проверка функцией hex : {hex(number)}')


def fun_trans_in_16(num):
    res = ""
    mod = num % SS
    while (mod > 0):
        if mod == TEN:
            res = "A" + res
        elif mod == ELEVEN:
            res = "B" + res
        elif mod == TWELVE:
            res = "C" + res
        elif mod == THIRTEEN:
            res = "D" + res
        elif mod == FOURTEEN:
            res = "E" + res
        elif mod == FIFTEEN:
            res = "F" + res
        else:
            res = str(mod) + res
        num //= SS
        mod = num % SS
    return res


trans_in_16()
