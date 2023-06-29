# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

array = [1, 1, 2, 1, 3, 5, 6, 7, 8, 2, 3, 4, 6]
array_result = []
array_double=[]

for item in array:
    if array.count(item)>1:
        array_double.append(item)
    else:
        array_result.append(item)






if __name__=='__main__':
    print(f'Список с дублирующимися элементами: {set(array_double)}')
    print(f'Результирующий список без дубликатов: {array_result}')