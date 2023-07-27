# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """Class Rectangle"""
    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        """Calculation perimetr of Rectangle"""
        return (self.width + self.height) * 2

    def calc_area(self):
        """Calculation area of Rectangle"""
        return self.width * self.height

    def __add__(self, other):
        """Addition  perimetr of two Rectangles"""
        perimetr = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other.width
        height = perimetr / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """subtraction  perimetr of two Rectangles"""
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimetr = self.calc_perimeter() - other.calc_perimeter()
        height = perimetr / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        return f'периметр {self.calc_perimeter()}, длина {self.width}, ширина {self.height}'

    def __eq__(self, other) -> bool:
        """Method for equality two Rectangles in Class Rectangle"""
        return self.calc_area() == other.calc_area()

    def __lt__(self, other):  # меньше
        return self.calc_area() < other.calc_area()

    def __le__(self, other):  # меньше
        return self.calc_area() >= other.calc_area()


if __name__ == '__main__':
    new_rect = Rectangle(5, 30)
    # print(new_rect.calc_area())
    # print(new_rect.calc_perimeter())

    new_square = Rectangle(10, 5)
    # print(new_square.calc_area())
    # print(new_square.calc_perimeter())
    print(new_rect + new_square)
    print(new_rect - new_square)
    print(new_rect <= new_square)
