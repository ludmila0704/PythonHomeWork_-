# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция
# возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def file_absolute_path(file_path: str):
    b, c = file_path.replace('"', '').split('.')
    *a, b = str(b).rsplit("\\", maxsplit=1)

    return (a, b, c)


if __name__ == "__main__":
    res_t = file_absolute_path(input('Введите абсолютный путь до файла: '))
    print(f'Получаем кортеж из трех элементов: {res_t}')
