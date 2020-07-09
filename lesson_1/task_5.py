revenue = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))

profit = revenue - costs

if profit > 0:
    print(f'Прибыль: {profit:.2f}')
    profitability = profit / revenue
    print(f'Рентабельность выручки: {profitability:.2f}')
    staff = int(input('Введите численность сотрудников фирмы: '))
    profit_staff = profit / staff
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_staff:.2f}')
else:
    print(f'Убыток: {profit:.2f}')
