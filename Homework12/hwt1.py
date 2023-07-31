#
#
import csv


class CheckFIO:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя  удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not (value.istitle() and value.isalpha()):
            raise ValueError(f'ФИО должно начинаться с заглавной буквы и состоять из букв.')


class Student:
    name_st = CheckFIO()
    lastname = CheckFIO()
    patronymic = CheckFIO()
    aver_mark = 0

    def __init__(self, name_st: str, patronymic: str, lastname: str, file: str = 'lessons.csv'):
        lessons = {}

        self.name_st = name_st
        self.lastname = lastname
        self.patronymic = patronymic
        with open(file, 'r', encoding='utf-8', newline='') as f:
            type_lesson = csv.reader(f)
            for item in type_lesson:
                lessons[item[0]] = {'marks': [], 'test': []}

        self.lessons = lessons


    def __str__(self):
        return f'Студент "{self.name_st} {self.patronymic} {self.lastname}",\nЖурнал оценок по предметам: {self.lessons}'

    def fill_mark(self, lesson: str, number: [int], check_type: str = 'marks'):

        if lesson not in self.lessons.keys():

            raise AttributeError('У студента нет данного предмета')

        for item in number:
            if check_type == 'marks' and (item < 2 or item > 5):
                raise ValueError('Такой оценки для урока не существует!!! Введите значение в дипазоне (2-5)')
            if check_type == 'test' and (item < 0 or item > 100):
                raise ValueError('Такой оценки для теста не существует!!!Введите значение в дипазоне (0-100)')
            self.lessons[lesson][check_type].append(item)

    def get_aver_mark_test(self):
        test_list = []
        sum_all_mark = 0
        count_mark_all = 0

        for lesson, values in self.lessons.items():
            avg_test = (sum(item) / len(item) for key, item in values.items() if (key == 'test' and len(item) != 0))

            sum_all_mark_les = ((sum(item), len(item)) for key, item in values.items() if (key == 'marks'))

            sum_mark, count_mark_l = next(sum_all_mark_les)
            sum_all_mark += sum_mark
            count_mark_all += count_mark_l
            test_list.append((lesson, *avg_test))

        if count_mark_all != 0:

            self.aver_mark = round(sum_all_mark / count_mark_all, 2)
            print(f'Cредняя оценка по всем предметам: {self.aver_mark}')
        print('Cредний балл по тестам для каждого предмета:')
        for item in test_list:
            if len(item) == 2:
                print(f'{item}')
            if len(item) == 1:
                print(f'{item[0]}: не заполнены результаты тестирований')


if __name__ == "__main__":
    student = Student('Иван', 'Иванович', 'Иванов')
    student.fill_mark('математика', [3, 5])
    student.fill_mark('биология', [4, 50, 42, 62], 'test')
    student.fill_mark('история', [4, 3, 4, 5])
    print(student)
    student.get_aver_mark_test()

