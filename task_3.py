def my_func(*args):
    """Выводит сумму наибольших двух аргументов."""
    print(sum(args) - min(args))


my_func(1, 100, 4)


# Реализация через анонимную функцию
print((lambda *args: sum(args) - min(args))(1, 100, 4))
