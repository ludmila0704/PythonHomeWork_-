#
def gen_fibbonacci(number: int):
    f0, f1 = 0, 1

    for i in range(abs(number) + 1):
        if number > 0:
            yield f0
        else:
            yield f0 * (-1) ** (i + 1)
        f0, f1 = f1, f0 + f1


if __name__ == "__main__":
    res=int(input("Введите число для вычисления последовательности Фибоначчи:  "))
    print(*gen_fibbonacci(res))
    for i, num in enumerate(gen_fibbonacci(res), start=0):
        print(f'f{i} = {num}',end=' ; ')
