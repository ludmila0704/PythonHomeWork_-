# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_spec(self):
        pass


class Fish(Animal):
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, long: int):
        if name.isalpha():
            super().__init__(name)
        else:
            raise AnimalNameError(name)
        if not isinstance(long, int):
            raise AnimalPropertyTypeError(name, long)
        if long > 0:
            self.long = long
        else:
            raise AnimalPropertyValueError(name, long)

    def show_spec(self):
        if self.long < self.LITTLE:
            return "Мелководная рыба"
        elif self.long > self.HIGHT:
            return "Глубоководная рыба"
        else:
            return "Средне-глубоководная рыба"


class Bird(Animal):
    def __init__(self, name: str, length: int):
        if name.isalpha():
            super().__init__(name)
        else:
            raise AnimalNameError(name)
        if not isinstance(length, int):
            raise AnimalPropertyTypeError(name, length)
        if length > 0:
            self.length = length
        else:
            raise AnimalPropertyValueError(name, length)
        self.length = length

    def show_spec(self):
        return self.length * 2


class AnimalException(Exception):
    pass


class AnimalPropertyTypeError(AnimalException):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'Свойство экземпляра класса {self.name}  должно быть целого типа '


class AnimalPropertyValueError(AnimalException):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'Значение свойства экземпляра класса {self.name}   должно быть положительным '


class AnimalNameError(AnimalException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Имя экземпляря класса {self.name} должно состоять только из букв '


if __name__ == "__main__":
    fish1 = Fish('akula', -3)

    bird1 = Bird('orel', 15.3)
    bird2 = Bird('wood12pecker', 30)
