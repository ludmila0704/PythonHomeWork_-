# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
import math
import fractions


def input_print():
    fraction1 = input('Введите  1 строкy  вида “a/b”:   ').split('/')
    fraction2 = input('Введите  2 строкy  вида “a/b”:   ').split('/')
    operation_frac(fraction1, fraction2)

def operation_frac(num1, num2):
    #Вычисление НОК через НОД по формуле: НОК=а*b/НОД(a,b)
    nok = (int(num1[1])* int(num2[1]))/ math.gcd(int(num1[1]), int(num2[1]))

    compos_frac = int(num1[0]) * (nok / int(num1[1])) + int(num2[0]) * (nok/ int(num2[1]))
    nod = math.gcd(int(compos_frac),int(nok))# для сокращения числителя и знаменателя
    mylti_frac_num = int(num1[0]) * int(num2[0]) #числитель
    mylti_frac_denom= int(num1[1]) * int(num2[1]) #знаменатель
    nod_mylti=math.gcd(mylti_frac_num,mylti_frac_denom)
    print(f'Сумма дробей равна {int(compos_frac/nod)} / {int(nok/nod)}')
    print(f'Проверка Fractions: {fractions.Fraction(int(num1[0]),int(num1[1]))+fractions.Fraction(int(num2[0]), int(num2[1]))}')
    print(f'Произведение дробей равно {int(mylti_frac_num/nod_mylti)} / {int(mylti_frac_denom/nod_mylti)}')
    print(
        f'Проверка Fractions: {fractions.Fraction(int(num1[0]), int(num1[1])) * fractions.Fraction(int(num2[0]), int(num2[1]))}')

input_print()