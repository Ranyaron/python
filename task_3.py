"""В пределах от 20 до 240 выводятся числа, кратные 20 или 21."""

my_numbers = [el for el in range(20, 240 + 1) if el % 20 == 0 or el % 21 == 0]

print(my_numbers)
