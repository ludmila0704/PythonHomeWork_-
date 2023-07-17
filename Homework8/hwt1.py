# файлы json, csv и pickle.

import os
import json
import csv
import pickle



def get_info_about_dir(dir: str) -> None:

    info_list = []
    for dir_path, folders_name, file_name in os.walk(dir):


        print(f'{dir_path = }\n{folders_name = }\n{file_name = }\n')

        for folder in folders_name:
            size = sum(os.path.getsize(os.path.join(dir_path, folder)) for f in os.listdir('.') if os.path.isfile(f))

            parents_name = os.path.dirname(os.path.join(dir_path, folder))
            info_list.append(
                {'name': folder, 'path': dir_path, 'size': size, 'file_or_dir': 'DIR', 'parent': parents_name})

        for file in file_name:
            file_size = os.path.getsize(os.path.join(dir_path, file))
            parents_name = (os.path.dirname(os.path.join(dir_path, file)))
            info_list.append(
                {'name': file, 'path': dir_path, 'size': file_size, 'file_or_dir': 'FILE', 'parent': parents_name})

        # print(info_list)


    with open('Hw1_json_file.json', 'w', encoding='utf-8') as f1, \
            open('Hw_1_csv_file.csv', 'w', encoding='utf-8') as f2, \
            open('Hw1_pickle_file.pickle', 'wb') as f3:
        json.dump(info_list, f1, indent=2)
        writer = csv.DictWriter(f2, fieldnames=['name', 'path', 'size', 'file_or_dir', 'parent'])
        writer.writeheader()
        writer.writerows(info_list)
        pickle.dump(f'{pickle.dumps(info_list)}', f3)


if __name__ == '__main__':
    get_info_about_dir('C:\PythonHomeWork_T')
