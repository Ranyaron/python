import re


class ComplexNumber:
    """Операции с комплексными числами"""
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        # return self.number + other.number

        number_1 = self.number.split()
        number_2 = other.number.split()
        if number_1[1] == "+" and number_2[1] == "+":
            self.number = re.findall(r"\d+", self.number)
            other.number = re.findall(r"\d+", other.number)
            sum_1 = int(self.number[0]) + int(other.number[0])
            sum_2 = int(self.number[1]) + int(other.number[1])
            return f"{sum_1} + {sum_2}i"
        elif number_1[1] == "+" and number_2[1] == "-":
            self.number = re.findall(r"\d+", self.number)
            other.number = re.findall(r"\d+", other.number)
            sum_1 = int(self.number[0]) + int(other.number[0])
            sum_2 = int(((int(self.number[1]) - int(other.number[1]))**2)**0.5)
            return f"{sum_1} - {sum_2}i"
        elif number_1[1] == "-" and number_2[1] == "+":
            self.number = re.findall(r"\d+", self.number)
            other.number = re.findall(r"\d+", other.number)
            sum_1 = int(self.number[0]) + int(other.number[0])
            sum_2 = int(((int(other.number[1]) - int(self.number[1]))**2)**0.5)
            return f"{sum_1} - {sum_2}i"
        elif number_1[1] == "-" and number_2[1] == "-":
            self.number = re.findall(r"\d+", self.number)
            other.number = re.findall(r"\d+", other.number)
            sum_1 = int(self.number[0]) + int(other.number[0])
            sum_2 = int(self.number[1]) + int(other.number[1])
            return f"{sum_1} - {sum_2}i"

    def __mul__(self, other):
        return self.number * other.number


complex_number_1_my = ComplexNumber("3 + 1i")
complex_number_2_my = ComplexNumber("2 - 3i")
print(complex_number_1_my + complex_number_2_my)

complex_number_1 = ComplexNumber(3 + 1j)
complex_number_2 = ComplexNumber(2 - 3j)
print(complex_number_1 * complex_number_2)
