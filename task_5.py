from functools import reduce


def my_func(prev_el, el):
    """Возвращает результат произведения элементов списка."""
    return prev_el + el


print(reduce(my_func, [el for el in range(100, 1000 + 1)]))
