class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        print(f'{self.name} {self.surname}, position {self.position}')

    def get_total_income(self):
        print(f'Premium income {sum(self.__income.values())} $')


pos = Position('Ilia', 'Chechulin', 'Machine Learning Engineer', 50000, 50000)
pos.get_full_name()
pos.get_total_income()
