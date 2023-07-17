# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
#

import json
import os
import pickle


def find_json_file_in_dir(dir: str) -> None:
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


if __name__ == "__main__":
    find_json_file_in_dir('C:\PythonHomeWork_T\seminar8')
