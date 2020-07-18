def full_sum():
    """Выводит сумму всех чисел, введенных пользователем"""
    def numbers_sum(num):
        """
        :param num: строка чисел
        :return: сумма чисел
        """
        for i in range(len(num)):
            num[i] = int(num[i])
        return sum(num)

    number = 0
    while True:
        try:
            numbers = input('Введите числа через пробел или "q" для выхода: ').split()
            if 'q' not in numbers:
                number += numbers_sum(numbers)
                print(number)
            elif 'q' in numbers[-1] and len(numbers) > 1:
                numbers.remove('q')
                number += numbers_sum(numbers)
                print(number)
                print('Программа завершена.')
                break
            else:
                print('Программа завершена.')
                break
        except ValueError:
            print('Error!')


full_sum()
