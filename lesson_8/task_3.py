import re


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
my_numbers = ""

while my_numbers != "q":
    my_numbers = input("Введите число: ")
    if my_numbers == "q":
        print("Программа завершена.")
        break
    numbers = my_numbers.split(" ")
    try:
        for i in numbers:
            for j in i:
                j = j.isalpha()
                if j:
                    raise OwnError("Вы ввели не число.")
    except OwnError as o_e:
        print(o_e)
    finally:
        my_list += re.findall(r'\d+', my_numbers)
        print(" ".join(my_list))
