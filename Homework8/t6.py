# преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# возьмите pickle версию файла из задачи# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import csv
import pickle


def get_pickle_file_to_scv(file1: str) -> None:
    # os.chdir(dir)
    # files_list = os.listdir(dir)
    #
    # for file_obj in files_list:
    #     #print(file_obj)
    #
    #     file_name, file_ext = os.path.splitext(file_obj)
    #     print(file_name, file_ext)
    #
    #     if file_ext.lower().endswith('.pickle'):
    with open(file1, 'rb') as fp:
        new_list = pickle.load(fp)

        # file_name_csv = f'{file_name}.scv'
        # if not os.path.exists(file_name_csv):
        #     with open(file_name_csv, 'wb') as f_csv:
        #         pickle.dump(new_dict, f_csv)
        all_data = []
        for row in new_list:
            headers_list = []
            value_list = []

            for header, value in row.items():
                headers_list.append(header)
                value_list.append(value)
            all_data.append(value_list)

        with open('t6.csv', 'w', encoding='utf-8') as f2:
            csv_write = csv.writer(f2, dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            csv_write.writerow(headers_list)
            csv_write.writerows(all_data)
            print(f'Сохранен файл {f2.name}')


if __name__ == "__main__":
    get_pickle_file_to_scv('new_json4.pickle')
