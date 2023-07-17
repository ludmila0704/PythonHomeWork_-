import json
import csv


def get_file_csv(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        my_dict = json.load(f)
        print(my_dict)
        my_list = []
        for level, value in my_dict.items():
            for id_num, name in value.items():

                my_list.append({'level': int(level), 'id': int(id_num), 'name': name})
                print(my_list)
        print(my_list)
    with open('my_csv.csv', 'w', newline='',encoding='utf-8') as fs:
        csv_writer = csv.DictWriter(fs, fieldnames=('level', 'id', 'name'),dialect='excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(my_list)


if __name__ == "__main__":
    get_file_csv('s8t2.json')
