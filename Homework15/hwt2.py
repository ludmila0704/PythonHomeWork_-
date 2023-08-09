import logging
import argparse
from datetime import datetime

logging.basicConfig(filename='log_t2.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)
MIN_DATE = 1
MAX_YEAR = 9999
MAX_DAY = 31
MAX_MONTH = 12


def parse():
    parser = argparse.ArgumentParser(prog='Задача 2 дз',
                                     description='Данный модуль проверяет существует ли введенная дата',
                                     epilog='Строка->Класс')
    parser.add_argument('-d', '--date', default='01.01.1970', type=str, help='Дата')

    args = parser.parse_args()
    if is_real_date(args.date):
        logger.info(f'{datetime.now()} Введенная дата {args.date} существует!')
        return True
    else:
        logger.error(f'{datetime.now()} Введенная дата {args.date} не существует!')
        return False


def is_real_date(date: str) -> bool:
    format_date = list(map(int, date.split('.')))
    day, month, year = format_date  # распаковка кортежа
    if not (MIN_DATE <= year <= MAX_YEAR and MIN_DATE <= month <= MAX_MONTH and MIN_DATE <= day <= MAX_DAY):
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and _is_leap_year(year) and day > 29:
        return False
    if month == 2 and not _is_leap_year(year) and day > 28:
        return False
    return True


def _is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == "__main__":
    print(parse())
