# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import shuffle as sh

COUNT_X = 8
COUNT_Y = 8
res_final = []
count_final = 0

def is_taken_g(pairs_list: [str]) -> bool:
    x = []
    y = []

    for i in pairs_list:
        x.append(int(i[:1]))
        y.append(int(i[-1]))


    is_taken = True
    for i in range(COUNT_X):
        for j in range(i + 1, COUNT_Y):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                is_taken = False

    return is_taken


def split_pairs(pairs: str) -> [str]:
    tmp = [i for i in pairs.split()]
    return tmp


def random_pairs():

    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    sh(x)
    sh(y)
    name = [''.join(str(x)) + ''.join(str(y)) for x, y in zip(x, y)]

    return name


def print_res(res_list: [str]):
    for item in res_list:
        print(item)


if __name__ == "__main__":
    print(is_taken_g(split_pairs(input("Введите 8 пар чисел (например, пара 18) через пробел (позиции ферзей на шахматной доске):  "))))
    # print(is_taken_g(split_pairs('17 24 32 48 56 61 73 85')))
    # print(is_taken_g(split_pairs('18 27 36 45 54 63 72 81')))

    while True:
        res = random_pairs()
        if is_taken_g(res) and count_final < 4:
            res_final.append(res)
            count_final += 1
        elif count_final >= 4:
            break

    print(f'Случайная успешная расстановка ферзей на позициях(не бьют друг друга): ')
    print_res(res_final)
