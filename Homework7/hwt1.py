# функцию группового переименования файлов. #


import os


def get_group_rename_files(count_digit_in_num: int, exp_start: str, exp_end: str,
                           range_name: list, desired_name='') -> None:
    files_list = os.listdir()
    count_file = 0
    for file_obj in files_list:
        if os.path.isfile(file_obj):
            file_name, file_exp = os.path.splitext(file_obj)
            print(file_name, file_exp)
            # end_name = ''
            index1, index2 = range_name

            count_file += 1
            if file_exp.lower().endswith((exp_start)):

                if index2 < len(file_name):
                    end_name = file_name[index1 - 1:index2]
                elif index1 <= len(file_name):
                    end_name = file_name[index1 - 1:len(file_name)]
                else:
                    end_name = ''

                res_count = "".join(["0"] * (count_digit_in_num - len(str(count_file)))) + str(count_file)

                end_name += desired_name + res_count + '.' + exp_end
                print(end_name)
                os.rename(file_obj, end_name)


if __name__ == "__main__":
    get_group_rename_files(3, 'txt', 'txt', [3, 5], 'new')
