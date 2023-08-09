# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
import logging
from datetime import datetime

import argparse

logging.basicConfig(filename='log_t3.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='Задача 3 дз',
                                     description='Данный модуль создание класса прямоугольники',
                                     epilog='Строка->Класс')
    parser.add_argument('-w', '--width', default=1, type=float, help='Длина')
    parser.add_argument('-he', '--height', type=float, help='Высота')
    # parser.add_argument('-h', '--height',default=0, type=float, help='Высота')

    args = parser.parse_args()
    return Rectangle(args.width, args.height)


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width: float, height: float = None):
        if (height is None or height <= 0) and width <= 0:
            logger.error(f'{datetime.now()} Прямоугольника сс сторонами {width} и {height} не существует ')
            raise RectangleNotExistError(width, height)
        if height is None and width > 0:
            self.height = width
            self.width = width
            logger.info(f'{datetime.now()} Создан прямоугольник со сторонами: {self.width},{self.height}')

        if width > 0 and height > 0:
            self.width = width
            self.height = height
            logger.info(f'{datetime.now()} Создан прямоугольник со сторонами: {self.width},{self.height}')

        else:
            logger.error(f'{datetime.now()} Прямоугольника сс сторонами {width} и {height} не существует ')
            raise RectangleNotExistError(width, height)

    def calc_perimeter(self):
        """Calculation perimetr of Rectangle"""
        logger.info(f'Периметр прямоугольника равен {(self.width + self.height) * 2}')
        return (self.width + self.height) * 2

    def calc_area(self):
        """Calculation area of Rectangle"""
        logger.info(f'Площадь прямоугольника равна {self.width * self.height}')
        return self.width * self.height

    def __str__(self):

        return f'периметр {self.calc_perimeter()}, площадь {self.calc_area()}, длина {self.width}, ширина {self.height}'


class RectangleException(Exception):
    pass


class RectangleNotExistError(RectangleException):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Прямоугольника сс сторонами {self.width} и {self.height} не существует '


if __name__ == '__main__':
    print(parse())
