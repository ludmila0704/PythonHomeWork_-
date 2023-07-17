# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json

TEN = 10


def read_file_csv_not_dict(file1: str, file2: str) -> None:
    with open(file1, 'r', newline='', encoding='utf-8') as f1:

        csv_file = csv.reader(f1, dialect='excel-tab')
        new_dict_all = []
        for i, line_list in enumerate(csv_file):

            if i != 0:
                new_dict = {}
                level, id_name, name = line_list
                new_dict['level']=int(level)
                new_dict['id_name'] = ''.join(["0"] * (TEN - len(str(id_name)))) + str(id_name)
                new_dict['name'] = name.capitalize()
                new_dict['hash'] = hash(f'{int(id_name)}{name}')

                new_dict_all.append((new_dict))
                print(new_dict)

        with open(file2, 'w', encoding='utf-8') as f2:
            json.dump(new_dict_all, f2, indent=2, separators=(',', ':'))


if __name__ == "__main__":
    read_file_csv_not_dict('my_csv.csv', 'new_json4.json')
