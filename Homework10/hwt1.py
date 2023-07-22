# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
class Fabric:
    def get_new(self, type: str, *args, **kwargs):
        new_animal = self.create_animal(type)
        return new_animal(*args, **kwargs)

    def create_animal(self, type: str):
        types = {"fish": Fish, "bird": Bird}
        return types[type.lower()]

    def get_info(self):
        pass


class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_spec(self):
        pass


class Fish(Animal):
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, long: int):
        super().__init__(name)
        self.long = long

    def show_spec(self):
        if self.long < self.LITTLE:
            return "Мелководная рыба"
        elif self.long > self.HIGHT:
            return "Глубоководная рыба"
        else:
            return "Средне-глубоководная рыба"


class Bird(Animal):
    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.length = length

    def show_spec(self):
        return self.length * 2


if 'name' == '__main__':
    # fish1 = Fish('akula', 50)
    # bird1 = Bird('orel', 15)
    # animal_list = [fish1, bird1]
    # for animal in animal_list:
    #     print(animal.show_spec())
    new_fabric = Fabric()
    carp = new_fabric.get_new('Fish', 'carp', 30)
    print(f'Создали экземпляр внутри переданного класса {type(carp)} и его свойство: {carp.show_spec()}')
    print(type(carp))
    print(carp.show_spec())
