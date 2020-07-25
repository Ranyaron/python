"""Создаем текстовый файл, записываем в него набор чисел, разделенных пробелами.
Программа подсчитывает сумму чисел в файле и выводит ее на экран."""

from random import randrange

try:
    with open('text_5.txt', 'w', encoding='utf-8') as file:
        my_random = [randrange(1, 100, 1) for i in range(9)]
        my_random = [str(i) for i in my_random]
        file.writelines(' '.join(my_random))
except IOError:
    print('An I / O error has occurred!')

try:
    with open('text_5.txt', encoding='utf-8') as file:
        my_list = []
        for line in file:
            my_list = line.split()
        for i, item in enumerate(my_list):
            my_list[i] = int(item)
        print(f'Сумма чисел в файле = {sum(my_list)}')
except IOError:
    print('An I / O error has occurred!')
