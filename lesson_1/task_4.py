number = int(input('Введите число: '))

max = number % 10

while number != 0:
    number //= 10
    a = number % 10
    if a > max:
        max = a

print(max)
