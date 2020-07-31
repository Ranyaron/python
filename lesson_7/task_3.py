class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number < other.number:
            return other.number - self.number
        else:
            return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        if self.number < other.number:
            return int(other.number / self.number)
        else:
            return int(self.number / other.number)

    def make_order(self, row):
        n = self.number
        while n > 0:
            print('*' * row)
            n -= row
            if n < row:
                print('*' * n)
                break


cell_1 = Cell(7)
cell_2 = Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print()
cell_1.make_order(4)
print()
cell_2.make_order(5)
