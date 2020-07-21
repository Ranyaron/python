from itertools import count, islice, cycle

# итератор, генерирующий целые числа, начиная с указанного
start = 3
finish = 12
finish -= start - 1
for i in islice(count(start), finish):
    print(i, end=' ')

print('\n' + '-' * 33)  # разделитель

# итератор, повторяющий элементы некоторого списка, определенного заранее
с = 0
for el in cycle(["element_1", 'element_22', 'element_333']):
    if с > 4:
        break
    print(el)
    с += 1
