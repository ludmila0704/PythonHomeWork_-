# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
MAX_NUMBER = 100000
res = ""


def number():
    number = int(input('Введите не отрицательное число меньше 100 тысяч : '))
    if 1 < number < MAX_NUMBER:
        # res =(is_simple_or_compos(number))
        print(is_simple_or_compos(number))
    else:
        print("Неверно. Введенное число не из указанного диапазона")


def is_simple_or_compos(num):
    res = ""
    for i in range(2, num):
        if num % i == 0:
            res = "Число составное"
            break
        else:
            res = "Число простое"

    return res


number()
