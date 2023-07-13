# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def convert(names_file: str, nums_file: str, result_file: str) -> None:
    with open(names_file, 'r', encoding='utf-8') as f1, \
            open(nums_file, 'r', encoding='utf-8') as f2, \
            open(result_file, 'w', encoding='utf-8') as f3:
        data_nums = f1.readlines()
        # print(data_nums)
        data_names = f2.readlines()
        for i in range(min(len(data_nums), len(data_names))):

            int_value, float_v = data_nums[i][:-2].split('|')

            int_value = int(int_value)
            float_v = float(float_v)
            mult_res = int_value * float_v
            if mult_res < 0:
                res = data_names[i][:-2].lower() + '' + str(abs(mult_res))
            else:
                res = data_names[i][:-2].upper() + '' + str(round(mult_res))

            f3.write(res + '\n')
        str_n = min(len(data_nums), len(data_names))
        len_div = max(len(data_nums), len(data_names)) - min(len(data_nums), len(data_names))
        is_long_names = len(data_names) > len(data_nums)
        if is_long_names:
            short = data_nums
            long = data_names
        else:
            short = data_names
            long = data_nums

        for i in range(len_div):
            if is_long_names:
                int_value, float_v = short[i].split('|')
                int_value = int(int_value)
                float_v = float(float_v)
                mult_res = int_value * float_v
                if mult_res < 0:
                    res = long[str_n + i][:-2].lower() + '' + str(abs(mult_res))
                else:
                    res = long[str_n + i][:-2].upper() + '' + str(round(mult_res))

            else:
                int_value, float_v = long[str_n + i].split('|')
                int_value = int(int_value)
                float_v = float(float_v)
                mult_res = int_value * float_v
                if mult_res < 0:
                    res = short[i].lower() + '' + str(abs(mult_res))
                else:
                    res = short[str_n + i].upper() + '' + str(round(mult_res))

            f3.write(res + '\n')


if __name__ == "__main__":
    convert('text.txt', 'text2.txt', 'res.txt')
