# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

res = ""


def input_sides_triangle():
    a = int(input('Введите 1 сторону треугольника: '))
    b = int(input('Введите 2 сторону треугольника: '))
    c = int(input('Введите 3 сторону треугольника: '))
    print(is_triangle(a, b, c))


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if (a == b or b == c or a == c):
            if a == c:
                return "Является равносторонним треугольником"
            else:
                return "Является равнобедренным треугольником"
        else:
            return "Является треугольником"

    else:
        return "Не является треугольником"


input_sides_triangle()