class Rectangle:
    """Class Rectangle"""

    def __init__(self, width: float, height: float = None):
        if width >= 0 and height >= 0:
            self.width = width
            self.height = height
        elif width >= 0 and height is None:
            self.height = width
        else:
            raise RectangleNotExistError(width, height)

    def calc_perimeter(self):
        """Calculation perimetr of Rectangle"""
        return (self.width + self.height) * 2

    def calc_area(self):
        """Calculation area of Rectangle"""
        return self.width * self.height

    def __str__(self):
        return f'периметр {self.calc_perimeter()}, длина {self.width}, ширина {self.height}'


class RectangleException(Exception):
    pass


class RectangleNotExistError(RectangleException):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Треугольник сс сторонами {self.width} и {self.height} не существует '


if __name__ == '__main__':
    new_rect = Rectangle(-10, 20)
    new_rect = Rectangle(-10)
