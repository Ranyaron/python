def fact(n):
    """
    Генератор, создающий очередное значение.

    :param n: факториала числа
    """
    for i in range(1, n + 1):
        yield i


f = 4
factorial = 1
for el in fact(f):
    factorial *= el

print(f'Факториал числа {f} = {factorial}')
