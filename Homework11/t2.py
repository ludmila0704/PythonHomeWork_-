# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Archive class"""
    __instance = None

    def __init__(self, num: int, text: str):
        """Init """
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """ creating a new instance"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __str__(self):
        return f'число = {self.num}, текст = {self.text},Архив_текст = {self.text_list}, Архив чисел ={self.num_list}'

    def __repr__(self):
        return f'число = {self.num}, текст = {self.text}'


if __name__ == "__main__":
    arc = Archive('text', 5)
    arc1 = Archive('text', 5)
    print(arc)

    print(arc)
    print(repr(arc))
    # print(Archive.__doc__)
