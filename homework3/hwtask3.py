# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

dict_things = {'мыло': 0.2, 'паста': 0.3, 'зубная щетка': 0.3, 'футболка': 0.5, 'аптечка': 0.8, 'полотенце': 0.6,
               'складной нож': 0.5,'вилка': 0.4, 'ложка': 0.4, 'кружка': 0.6, 'миска': 0.7, 'котелок': 1.5,\
               'мешки для мусора': 0.3, 'фонарик': 0.9, 'компас': 0.4, 'спички': 0.8}

MAX_MASSA = 1.5
list_tesult = []

temp_massa = 0
temp_list = []
for key, value in dict_things.items():

    if temp_massa <= MAX_MASSA:
        for key_n, value_n in dict_things.items():
            if temp_massa + value_n <= MAX_MASSA:
                temp_massa += value_n
                list_tesult.append(key_n)


if __name__=='__main__':
    print(f'В рюкзак вмещаются (не более {MAX_MASSA}кг):{(list_tesult)},их общая масса равна {temp_massa}')