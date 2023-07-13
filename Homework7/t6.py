# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.

import os
from random import choices, randint
from string import ascii_lowercase, digits


def gen_many_exc_many_count(exc: [str], count_files: [int], dir_input: str) -> None:
    def gen_ext(ext: str, name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096,
                num_files: int = 42) -> None:
        for _ in range(num_files):
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
            data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
            with open(f'{name}.{ext}', 'wb') as f:
                if not os.path.exists('f'):
                    f.write(data)

    if os.path.exists(dir_input):
        os.chdir(dir_input)

    else:
        os.mkdir(dir_input)
        os.chdir(dir_input)

    _ = (gen_ext(exc, num_files=count) for (exc, count) in zip(exc, count_files))
    print(*_)


if __name__ == '__main__':

    gen_many_exc_many_count(['jpg', 'mp4', 'avi'], [1, 2, 1], 'C:\PythonHomeWork_T\seminar7')
