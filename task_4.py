def my_func(x, y):
    """Возведение числа x в степень y.

    :param x: действительное положительное число
    :param y: целое отрицательное число
    """
    if y > 0:
        y -= y * 2
    print(x ** y)
    x = abs(x)
    number = x
    z = 1
    while abs(y) != z:
        number *= x
        z += 1
    print(round((1 / number), 5))


my_func(4, -2)
