def numbers_division():
    """Выводит результат частного от деления."""
    try:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        print(f'{x} / {y} = {x / y}')
    except ZeroDivisionError:
        print('Делить на ноль нельзя.')
    except ValueError:
        print('Error!')


numbers_division()


# Подскажите, будет ли эта функция считаться полноценной?
#
# def numbers_division(a, b):
#     """
#     Возвращает частное от деления.
#
#     (number, number) -> number
#
#     >>> numbers_division(10, 2)
#     5.0
#     """
#     return a / b
#
#
# try:
#     number_1 = int(input('Введите первое число: '))
#     number_2 = int(input('Введите второе число: '))
#     print(f'{number_1} / {number_2} = {numbers_division(number_1, number_2)}')
# except ZeroDivisionError:
#     print('Делить на ноль нельзя.')
# except ValueError:
#     print('Error!')
