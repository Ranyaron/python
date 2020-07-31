from abc import ABC, abstractmethod


class Clothes(ABC):
    cloth = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = round((v / 6.5 + 0.5), 2)

    @property
    def cloth_coat(self):
        return f'Расход ткани для пошива {self.name} составит {self.v}'

    def calc_cloth(self):
        Clothes.cloth += self.v


class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = round((2 * h + 0.3), 2)

    @property
    def cloth_costume(self):
        return f'Расход ткани для пошива {self.name} составит {self.h}'

    def calc_cloth(self):
        Clothes.cloth += self.h


coat = Coat('Grizzlies', 48)
costume = Costume('Lion', 173)

print(coat.cloth_coat)
print(costume.cloth_costume)

coat.calc_cloth()
costume.calc_cloth()

print(f'Общий расход ткани: {coat.cloth}')
