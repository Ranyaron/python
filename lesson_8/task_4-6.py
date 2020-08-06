# OEW == OfficeEquipmentWarehouse
class OEW:
    """Склад оргтехники"""
    OEW_dict = {
        "Printer": {
            1: {"name": "printer_1", "color": "red", "series": "123", "count": 3},
            2: {"name": "printer_2", "color": "black", "series": "456", "count": 6}
        },
        "Scanner": {
            1: {"name": "scanner_1", "color": "red", "series": "123", "count": 3},
            2: {"name": "scanner_2", "color": "black", "series": "456", "count": 6}
        },
        "Xerox": {
            1: {"name": "xerox_1", "color": "red", "series": "123", "count": 3},
            2: {"name": "xerox_2", "color": "black", "series": "456", "count": 6}
        }
    }

    def reception(self, name, category):
        """Приём оргтехники на склад"""
        for i in range(len(OEW.OEW_dict[category])):
            if name["name"] == OEW.OEW_dict[category][i + 1]["name"] \
                    and name["color"] == OEW.OEW_dict[category][i + 1]["color"] \
                    and name["series"] == OEW.OEW_dict[category][i + 1]["series"] \
                    and name["test"] == OEW.OEW_dict[category][i + 1]["test"]:
                OEW.OEW_dict[category][i + 1]["count"] += name["count"]
                printer_name = OEW.OEW_dict[category][i + 1]["name"]
                printer_count = OEW.OEW_dict[category][i + 1]["count"]
                print(f"Кол-во принтеров {printer_name} обновлено. На складе {printer_count} шт.")
                break
            if name["name"] != OEW.OEW_dict[category][i + 1]["name"] \
                    or name["color"] != OEW.OEW_dict[category][i + 1]["color"] \
                    or name["series"] != OEW.OEW_dict[category][i + 1]["series"] \
                    or name["test"] == OEW.OEW_dict[category][i + 1]["test"]:
                continue
        else:
            OEW.OEW_dict[category][len(OEW.OEW_dict[category]) + 1] = name
            printer_name = name["name"]
            print(f"Добавлен новый принтер: {printer_name}")

    def broadcast(self, name, category):
        """Передача оргтехники в определенное подразделение компании"""
        for i in range(len(OEW.OEW_dict[category])):
            if name["name"] == OEW.OEW_dict[category][i + 1]["name"] \
                    and name["color"] == OEW.OEW_dict[category][i + 1]["color"] \
                    and name["series"] == OEW.OEW_dict[category][i + 1]["series"] \
                    and name["test"] == OEW.OEW_dict[category][i + 1]["test"]:
                OEW.OEW_dict[category][i + 1]["count"] -= name["count"]
                if OEW.OEW_dict[category][i + 1]["count"] < 0:
                    print("На складе нет такого количества. Попробуйте еще раз.\n")
                    OEW.OEW_dict[category][i + 1]["count"] += name["count"]
                    break
                printer_name = OEW.OEW_dict[category][i + 1]["name"]
                printer_count = OEW.OEW_dict[category][i + 1]["count"]
                print(f"Кол-во принтеров {printer_name} обновлено. На складе {printer_count} шт.")
                break


class OfficeEquipment:
    """Оргтехника"""
    def __init__(self, name, color, series, count):
        self.name = name
        self.color = color
        self.series = series
        self.count = count


class Printer(OfficeEquipment):
    def __init__(self, name, color, series, count, test):
        super().__init__(name, color, series, count)
        self.list = {'name': name, 'color': color, 'series': series, "count": count, "test": test}

    def printer_list(self):
        return self.list


class Scanner(OfficeEquipment):
    def __init__(self, name, color, series, count):
        super().__init__(name, color, series, count)
        self.list = {'name': name, 'color': color, 'series': series, "count": count}

    def scanner_list(self):
        return self.list


class Xerox(OfficeEquipment):
    def __init__(self, name, color, series, count):
        super().__init__(name, color, series, count)
        self.list = {'name': name, 'color': color, 'series': series, "count": count}

    def xerox_list(self):
        return self.list


choice_1 = ""
while choice_1 != "q":
    try:
        choice_1 = input("Что Вы хотите сделать (введите число):\n"
                         "1 - Отправить оргтехнику на склад | "
                         "2 - Передать оргтехнику в подразделение компании | "
                         "q - Выход\n")
        if choice_1 == "1":
            choice_2 = input("Что отправить на склад (введите число): "
                             "1 - Принтер | "
                             "2 - Сканер | "
                             "3 - Ксерокс\n")
            if choice_2 == "1":
                choice_3 = input("Введите через пробел название принтера, его цвет и серию and test\n").split()
                category = "Printer"
                name = choice_3[0]
                color = choice_3[1]
                series = choice_3[2]
                count = int(input("Введите кол-во: "))
                test = choice_3[3]
                printer = Printer(name, color, series, count, test)
                OEW().reception(printer.printer_list(), category)
            elif choice_2 == "2":
                choice_3 = input("Введите через пробел название сканера, его цвет и серию\n").split()
                category = "Scanner"
                name = choice_3[0]
                color = choice_3[1]
                series = choice_3[2]
                count = int(input("Введите кол-во: "))
                scanner = Scanner(name, color, series, count)
                OEW().reception(scanner.scanner_list(), category)
            elif choice_2 == "3":
                choice_3 = input("Введите через пробел название ксерокса, его цвет и серию\n").split()
                category = "Xerox"
                name = choice_3[0]
                color = choice_3[1]
                series = choice_3[2]
                count = int(input("Введите кол-во: "))
                xerox = Xerox(name, color, series, count)
                OEW().reception(xerox.xerox_list(), category)
        elif choice_1 == "2":
            choice_2 = input("Что передать в подразделение (введите число):\n"
                             "1 - Принтер | "
                             "2 - Сканер | "
                             "3 - Ксерокс\n")
            if choice_2 == "1":
                print("Выберите интерисующую модель (введите число):\nПринтеры:")
                for key, value in OEW.OEW_dict["Printer"].items():
                    print(f"{key}: {value}")
                choice_3 = input()
                choice_3 = OEW.OEW_dict["Printer"][int(choice_3)]
                category = "Printer"
                name = choice_3["name"]
                color = choice_3["color"]
                series = choice_3["series"]
                count = int(input("Введите кол-во: "))
                test = choice_3["test"]
                printer = Printer(name, color, series, count, test)
                OEW().broadcast(printer.printer_list(), category)
            elif choice_2 == "2":
                print("Выберите интерисующую модель (введите число):\nСканеры:")
                for key, value in OEW.OEW_dict["Scanner"].items():
                    print(f"{key}: {value}")
                choice_3 = input()
                choice_3 = OEW.OEW_dict["Scanner"][int(choice_3)]
                category = "Scanner"
                name = choice_3["name"]
                color = choice_3["color"]
                series = choice_3["series"]
                count = int(input("Введите кол-во: "))
                scanner = Scanner(name, color, series, count)
                OEW().broadcast(scanner.scanner_list(), category)
            elif choice_2 == "3":
                print("Выберите интерисующую модель (введите число):\nКсероксы:")
                for key, value in OEW.OEW_dict["Xerox"].items():
                    print(f"{key}: {value}")
                choice_3 = input()
                choice_3 = OEW.OEW_dict["Xerox"][int(choice_3)]
                category = "Xerox"
                name = choice_3["name"]
                color = choice_3["color"]
                series = choice_3["series"]
                count = int(input("Введите кол-во: "))
                xerox = Xerox(name, color, series, count)
                OEW().broadcast(xerox.xerox_list(), category)
    except ValueError:
        print("Вы ввели не число.")
else:
    print("Программа завершена.")
