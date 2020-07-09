print('Привет, это КАЛЬКУЛЯТОР :)')
number_a = int(input('Введите первое число: '))
number_b = int(input('Введите второе число: '))
number_operation = input('Что Вы хотите сделать (+, -, *, /): ')

if number_operation == '+':
    print(number_a + number_b)
elif number_operation == '-':
    print(number_a - number_b)
elif number_operation == '*':
    print(number_a * number_b)
elif number_operation == '/':
    print(number_a / number_b)
else:
    print('Вы ввели не верное значение.')
