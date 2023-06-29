# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
import random

COUNT_FRIEND = 3
dict_fr_things = {}
friends = ['Вася', 'Коля', 'Петя']
things_in_bag = ['мыло', 'паста', 'зубная щетка', 'футболка', 'аптечка', 'полотенце', 'складной нож', \
                 'вилка', 'ложка', 'кружка', 'миска', 'котелок', 'мешки для мусора', 'фонарик', 'компас', 'спички']

for name in friends:
    dict_fr_things[name] = (random.choice(things_in_bag), random.choice(things_in_bag), random.choice(things_in_bag), \
                            random.choice(things_in_bag), random.choice(things_in_bag), random.choice(things_in_bag))
# dict_fr_things={'Вася': ('полотенце', 'паста', 'зубная щетка', 'компас', 'котелок'),
#                  'Коля': ('миска', 'паста', 'компас', 'спички', 'ложка', 'кружка'),
#                  'Петя': ('фонарик', 'аптечка', 'компас', 'футболка', 'мыло', 'складной нож','паста')}

print(dict_fr_things)

not_unique_thing = set()
not_have_one = set()
mylist = []  # список предметов
for key in dict_fr_things:
    mylist.extend(list(dict_fr_things[key]))

for key, value in dict_fr_things.items():
    for i in range(len(value)):
        if mylist.count(value[i]) == 1:
            print(f'{key} носит в рюкзаке уникальный предмет - {value[i]}.')
        if mylist.count(value[i]) == len(dict_fr_things):
            not_unique_thing.add(value[i])
        if mylist.count(value[i]) == len(dict_fr_things) - 1:
            not_have_one.add(value[i])
for key, value in dict_fr_things.items():
    for i in not_have_one:
        if i not in dict_fr_things[key]:
            print(f'{key} не взял с собой {i}')
print(f'Вещи, которые взяли все три друга: {not_unique_thing}')
