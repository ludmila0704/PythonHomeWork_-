import logging
from os import path
from datetime import datetime
import os
import argparse

logging.basicConfig(filename='log_t1.log', style='{', level=logging.INFO,encoding='utf-8')
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='Задача 1 дз', description='Данный модуль создает класс Person',
                                     epilog='Строка->Класс')
    parser.add_argument('-n', '--last_name', default='', type=str, help='Имя')
    parser.add_argument('-f', '--fers_name', default='', type=str, help='Фамилия')
    parser.add_argument('-p', '--patronomic', default='', type=str, help='Отчество')
    parser.add_argument('-a', '--age', default=1, type=int, help='Сколько лет')
    args = parser.parse_args()

    return Person(args.last_name, args.fers_name, args.patronomic, args.age)


class Person:
    def __init__(self, last_name: str, fers_name: str, patronomic: str, age=int):
        if last_name.istitle() and fers_name.istitle() and patronomic.istitle():

            self.last_name = last_name
            self.fers_name = fers_name
            self.patronomic = patronomic

        else:
            logger.error(
                f'{datetime.now()} ValueError: ФИО {last_name} {fers_name} {patronomic} должно начинаться с заглавной буквы. ')
            raise ValueError('ФИО должно начинаться с заглавной буквы')

        if not isinstance(age, (int, float)):
            logger.error(f'{datetime.now()} TypeError: Возраст {age} должен быть числом. ')
            raise TypeError(f'Возраст должен быть числом.')

        elif age < 0:
            logger.error(f'{datetime.now()} ValueError: Возраст {age} должен быть положительным. ')
            raise ValueError(f'Возраст должен быть положительным.')

        else:
            self.__age = age
            logger.info(
                f'Создан экземпляр класса Person c именем {self.last_name},фамилией {self.fers_name}, отчеством {self.patronomic},лет: {self.__age}')

    def full_name(self):
        return f'Полное имя экземпляра класса: {self.last_name}{self.fers_name}{self.patronomic}'

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print(parse().full_name())
