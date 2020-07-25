try:
    with open('text_3.txt', encoding='utf-8') as file:
        my_dict = {}
        average_employee_income = 0
        full_average_employee_income = 0
        i = 0
        e = 0
        for line in file:
            my_dict.update(map(tuple, [line.split()]))
        try:
            print('Employees with a salary of less than 20,000:')
            for key, value in my_dict.items():
                if float(value) < 20000.00:
                    print(f'{key} {value}')
                    average_employee_income += float(value)
                    i += 1
                full_average_employee_income += float(value)
                e += 1
            print(f'Average employee income: {round((average_employee_income / i), 2)}')
            print(f'\nAverage income of all employees: {round((full_average_employee_income / e), 2)}')
        except ValueError:
            print('Oops... There is an error in the data.\nFor example, numbers are mixed with symbols "10000;03abГд".')
except IOError:
    print('An I / O error has occurred!')
