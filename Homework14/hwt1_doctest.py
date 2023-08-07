class Person:
    """
    >>> person1.get_age()
    35
    >>> person1.full_name()
    'Ivanov Ivan Ivanovich'
    >>> person2.full_name()
    'Petrov Petr Petrovich'
    >>> person2.get_age()
    3
    """

    def __init__(self, last_name: str, fers_name: str, patronomic: str, age=int):
        if last_name.istitle() and fers_name.istitle() and patronomic.istitle():

            self.last_name = last_name
            self.fers_name = fers_name
            self.patronomic = patronomic
        else:
            raise ValueError('ФИО должно начинаться с заглавной буквы')
        if not isinstance(age, (int, float)):
            raise TypeError(f'Возраст должен быть числом.')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным.{age =}')
        else:
            self.__age = age

    def full_name(self):
        return f'{self.last_name} {self.fers_name} {self.patronomic}'

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    person1 = Person('Ivanov', 'Ivan', 'Ivanovich', 35)
    person2 = Person('Petrov', 'Petr', 'Petrovich', 2)
    person2.birthday()

    import doctest

    doctest.testmod(verbose=True)
