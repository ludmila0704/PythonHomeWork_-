from time import time


class My_string(str):
    """class My String"""

    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time_created = time()
        print(f'Cоздан класс {cls}')
        return instance
    def __str__(self):
        return f'author {self.author}, time {self.time_created}'


if __name__ == "__main__":
    new_str = My_string('Hello world', 'Jonny')
    print(new_str)

