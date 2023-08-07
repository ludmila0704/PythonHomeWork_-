# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст

class Person:
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
    print(person1)
    # person2=Person('ivanov','Ivan','Ivanovich',35)
    # person2=Person('Petrov','Saveliy','Petrovich',-22)
