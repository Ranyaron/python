from sys import argv


def employee_payroll():
    """
    Расчет заработной платы сотрудника.

    ставка в час * выработка в часах + премия

    :return: int(зарплата сотрудника)
    """
    script_name, first_param, second_param, third_param = argv
    return int(first_param) * int(second_param) + int(third_param)


print(employee_payroll())
