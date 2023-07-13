#  Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.

import os


def sort_on_dir(dir: str):
    if os.path.exists(dir):
        os.chdir(dir)
    else:
        os.mkdir(dir)
        os.chdir(dir)

    files_list = os.listdir()

    new_dir = ['foto', 'video', 'text_file']
    _ = (os.mkdir(i_dir) for i_dir in new_dir if not os.path.exists(i_dir))
    print(*_)

    for file_obj in files_list:
        file_name, file_ext = os.path.splitext(file_obj)
        if file_ext.lower().endswith(('.png', '.jpg', '.jpeg')):
            os.replace(file_obj, os.path.join(os.getcwd(), 'foto', file_obj))

        if file_ext.lower().endswith(('.mp4', '.avi', '.mov')):
            os.replace(file_obj, os.path.join(os.getcwd(), 'video', file_obj))

        if file_ext.lower().endswith(('.txt', '.json', '.rtf')):
            os.replace(file_obj, os.path.join(os.getcwd(), 'text_file', file_obj))


if __name__ == '__main__':
    sort_on_dir('C:\PythonHomeWork_T\seminar9')
