from random import randint as rint
from sys import argv


def guess_number(min_num: int, max_num: int, counts: int) -> bool:
    number = rint(min_num, max_num)

    for count in range(counts):
        current_num = int(input('Введите число: '))
        if current_num < number:
            print('искомое число больше этого ')
        elif current_num > number:
            print('искомое число меньше этого ')
        else:
            print("Вы угадали")
            return True

    print('Попытки закончились, вы не угадали')
    return False


if __name__ == "__main__":
    guess_number(10, 100, 10)
    # x = (int(i) for i in argv[:1])
    # guess_number(*x)
