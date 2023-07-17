# csv файл без# использования csv.DictReader.
#  pickle строку
import csv
import pickle


def get_csv_file_to_pickle_string(file1: str) -> None:
    with open(file1, 'r', encoding='utf-8', newline='') as f_csv:
        csv_file = csv.reader(f_csv)
        res_str = ''
        for line in csv_file:
            for item in line:
                res_str += item

        res = pickle.dumps(res_str, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'Pickle строка:   {res = }')


if __name__ == "__main__":
    get_csv_file_to_pickle_string('t6.csv')
