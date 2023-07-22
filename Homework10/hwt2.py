# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

import json
import os
import pickle
import csv


class File():

    def get_txt_to_json(self, path: str):
        my_dict = {}
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                print(line)
                name, number = line.split(' ')
                my_dict[name.capitalize()] = float(number)
        print(my_dict)
        with open('get_txt_to_json.json', 'w', encoding='utf-8') as f2:
            json.dump(my_dict, f2, ensure_ascii=False)

        # return pass

    def get_json_file_to_pickle(self, dir: str):
        os.chdir(dir)
        files_list = os.listdir(dir)

        for file_obj in files_list:

            file_name, file_ext = os.path.splitext(file_obj)

            if file_ext.lower().endswith('.json'):
                data = {}
                print(file_name)
                with open(file_obj, 'r', encoding='utf-8') as fjson:
                    data = json.load(fjson)
                    print(data)
                    file_name_pic = f'{file_name}.pickle'
                    if not os.path.exists(file_name_pic):
                        with open(file_name_pic, 'wb') as f_p:
                            pickle.dump(data, f_p)

    def get_csv_file_to_pickle_string(self, file1: str):
        with open(file1, 'r', encoding='utf-8', newline='') as f_csv:
            csv_file = csv.reader(f_csv)
            res_str = ''
            for line in csv_file:
                for item in line:
                    res_str += item

            res = pickle.dumps(res_str, protocol=pickle.DEFAULT_PROTOCOL)
            return (f'Pickle строка:   {res = }')


if __name__ == '__main__':
    file = File()
    file.get_json_file_to_pickle('C:\PythonHomeWork_T\seminar10')
    file.get_txt_to_json('res.txt')
    print(file.get_csv_file_to_pickle_string('t6.csv'))
