# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.

data = input('Введите строку:  ')
text_dict={}
text_dict1={}
##без  метода count
char_count=0
print(set(data))
for item in set(data):
    char_count = 0
    for item2 in data:
        if item2 ==item:
            char_count+=1
            text_dict[item] = char_count



#с методом count

for item in data:
    if item in set(data):
        text_dict1[item]=data.count(item)

print(text_dict1)

if __name__=='__main__':
    print('без  метода count')
    print(text_dict)
    print('с методом count')
    print(text_dict1)