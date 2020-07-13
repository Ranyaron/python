"""Значения обмениваются элементами с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохраняется на своем месте."""

my_list = input('Введите значения через пробел: ')
my_list = my_list.split()
print(my_list)

a = 1
for i in my_list[1::2]:
    my_list[a], my_list[a - 1] = my_list[a - 1], my_list[a]
    a += 2

# a = 0
# for i in range(int(len(my_list) / 2)):
#     my_list[a], my_list[a + 1] = my_list[a + 1], my_list[a]
#     a += 2

print(my_list)
