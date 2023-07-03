# банкомат.
#
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
MULT = 50
PERCENT = 0.015
EXTRA_PERCENT = 0.03
MIN_CASH = 30
MAX_CASH = 600
count_oper = 0  # количество операций клиента
MAX_COUNT = 3  # максимальное количество операций клиента
MAX_SCORE = 5_000_000
RICH_PERCENT = 0.1
total_score = 0
client_list = []
client_list.append(total_score)
client_list.append(count_oper)
list_operation = []


def menu():  # меню
    print_balance(client_list)
    print(' 1. Пополнить \n 2. Снять \n 3. Вывести операции по счету \n 4. Выйти')
    button = int(input('Выберите пункт: '))
    if button == 1:
        tax_on_luxury(client_list)
        add_cash(client_list)

    elif button == 2:
        check_Balance(client_list)
        tax_on_luxury(client_list)
        give_cash(client_list)
    elif button == 3:
        print_list_operation(list_operation)
        menu()
    elif button == 4:
        print('Вы выбрали выход!До скорых встреч!')
        exit()
    else:
        menu()


def tax_on_luxury(array_num):  # Налог на роскошь
    if array_num[0] <= MAX_SCORE:
        return
    elif array_num[0] > MAX_SCORE:
        array_num[0] = array_num[0] - array_num[0] * RICH_PERCENT
        list_operation.append('-' + str(array_num[0] * RICH_PERCENT))
        print(f'У вас вычтен налог на роскошь в размере - {100 * RICH_PERCENT} %')
        print_balance(array_num)


def check_Balance(array_num):  # Проверка баланса
    if array_num[0] <= 0:
        print("На вашем счет недостаточно средств для снятия наличных")
        menu()


def print_balance(array_num):  # баланс
    print(f'Ваш баланс: {array_num[0]} у.е. \n')
    return


#
def add_cash(array_num):  # Внесение наличных add cash
    money_inp = int(input('Внесите купюры кратные 50 у.е.: '))
    if money_inp % MULT == 0 and money_inp > 0:
        array_num[0] = array_num[0] + money_inp
        array_num[1] += 1
        list_operation.append('+' + str(money_inp))
        menu()
    else:
        print('Вы указали некорректную сумму.')
        menu()


def print_list_operation(list_oper):
    for item in list_oper:
        print(item, end=',')


#
def give_cash(array_num):  # Снятие наличных  give cash
    money_inp = float(input('Укажите сумму, которую хотите снять: '))
    if (money_inp > 0 and money_inp % MULT == 0):

        if array_num[1] % MAX_COUNT == 0:
            if ((money_inp + money_inp * EXTRA_PERCENT) <= array_num[0]) and MIN_CASH <= money_inp * EXTRA_PERCENT <= MAX_CASH:
                array_num[0] = float(array_num[0]) - money_inp - money_inp * EXTRA_PERCENT
                print(f'Вы сняли {money_inp}  у.е.')
                list_operation.append('-' + str(money_inp))
                array_num[1] += 1
            else:
                print('Данная сумма не доступна для снятия')
                print_balance(array_num)
        else:
            if ((money_inp + money_inp * PERCENT) <= array_num[0]) and MIN_CASH <= money_inp <= MAX_CASH:
                array_num[0] = float(array_num[0]) - money_inp - money_inp * PERCENT
                array_num[1] += 1
                list_operation.append('-' + str(money_inp))
                print(f'Вы сняли {money_inp}  у.е.')
            else:
                print('Денег на вашем счете недостаточно. Пополните счет.')
            print_balance(array_num)
            menu()

    else:
        print('Вы указали некорректную сумму')
        print_balance(array_num)
        menu()
    return


#
def start_win():  # Приветствие
    print("Вас приветствует БАНКОМАТ!!! ")
    menu()


if __name__ == '__main__':
    start_win()
