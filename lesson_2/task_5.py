"""Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением размещается после них."""

my_list = [21, 16, 7, 5, 3, 3, 2]
print(my_list)

while True:
    number = float(input('Введите число: '))
    if my_list[-1] > number:
        my_list.append(number)
    elif number in my_list:
        my_list.reverse()
        ind = my_list.index(number)
        my_list.insert(ind, number)
        my_list.reverse()
    else:
        for i in my_list:
            if number > i:
                ind = my_list.index(i)
                my_list.insert(ind, number)
                break
    print(my_list)
