"""Структура данных «Товары» - представляет собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже два элемента — номер товара и словарь с параметрами
(характеристики товара: название, цена, количество, единица измерения).
Программа собирает аналитику о товарах - это словарь,
в котором каждый ключ — характеристика товара, а значение — список значений-характеристик."""

my_list = []
my_dict = {}

name_input = ''
price_input = ''
quantity_input = ''
units_input = ''
output = ''
n = 1

while output != 'q':
    name_input = input('Введите название товара: ')
    while name_input == '':
        name_input = input('Введите название товара: ')

    Input = False
    while not Input:
        price_input = input('Введите стоимость товара: ')
        for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if i in price_input:
                Input = True
                break
    price_input = int(price_input)

    Input = False
    while not Input:
        quantity_input = input('Введите количество: ')
        for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if i in quantity_input:
                Input = True
                break
    quantity_input = int(quantity_input)

    units_input = input('Введите единицы измерения: ')
    while units_input == '':
        units_input = input('Введите единицы измерения: ')

    output = input('Выйти "q" или продолжить "enter": ')

    my_dict_tuple = {}
    my_dict_tuple.update({'название': name_input, 'цена': price_input, 'количество': quantity_input, 'eд': units_input})
    my_tuple = (n, my_dict_tuple)
    my_list.append(my_tuple)
    n += 1
    print('---------------------------------')  # Завершение цикла ввода данных

name = []
price = []
quantity = []
units = []

for i in range(len(my_list)):
    name.append(my_list[i][1].get('название'))
    price.append(my_list[i][1].get('цена'))
    quantity.append(my_list[i][1].get('количество'))
    units.append(my_list[i][1].get('eд'))

units = list(set(units))

my_dict.update({'Название': name, 'Цена': price, 'Количество': quantity, 'Ед': units})

print(f'Вывод аналитики\n---------------------------------')
for key, value in my_dict.items():
    print(f'{key}: {value}')


# Второй вариант цикла по вводу данных
# while output != 'q':
#     name_input = input('Введите название товара, его стоимость, количество и единицы измерения: ')
#     if name_input == '':
#         print('Вы ничего не ввели.')
#         continue
#
#     if ',' in name_input:
#         name_input = name_input.split(', ')
#     else:
#         name_input = name_input.split('')
#
#     name_input[1] = int(name_input[1])
#     name_input[2] = int(name_input[2])
#
#     output = input('Выйти "q" или продолжить "enter": ')
#
#     my_dict_tuple = {}
#     my_dict_tuple.update({'название': name_input[0], 'цена': name_input[1],
#                           'количество': name_input[2], 'eд': name_input[3]})
#     my_tuple = (n, my_dict_tuple)
#     my_list.append(my_tuple)
#     n += 1
#     print('---------------------------------')  # Завершение цикла ввода данных
